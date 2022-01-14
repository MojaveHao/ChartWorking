from PySide2.QtCore import *
import sys,os,shutil
import usefultools as ult
from PySide2.QtWidgets import *
import json
from pyecharts import Bar, Line, Pie
from ui_ChartWorkingWindow import Ui_MainWindow
class ChartWorking(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pbtn_OpenData.clicked.connect(self.select_file)
        self.pbtn_SelectData.clicked.connect(self.save)
        self.pbtn_render.clicked.connect(self.plot)
        self.pbtn_ok_x.clicked.connect(self.get_data)
        self.pbtn_ok_y.clicked.connect(self.get_data)
        self.pbtn_oklang.clicked.connect(self.select_lang)
        self.lang = 0
    def get_data(self):
        self.x = self.ledit_x.text()
        self.y = self.ledit_y.text()
        print(self.x,self.y)
        self.ChartProgress.reset()
    def select_file(self):
        self.data_file,_ = QFileDialog.getOpenFileName(caption=write_lang_ui("从文件导入数据"),filter="(*.json)")
        self.x = ult.json_rw(self.data_file)[0]
        self.y = ult.json_rw(self.data_file)[1]
        print(self.x,self.y)
        
    def plot(self):
        index_text = self.cbox_Type.currentText()
        if self.x and self.y:
            print(self.write_lang_ui("使用用户输入的数据").format(self.x,self.y),"type:{}".format(index_text))
            try:
                if int(self.x) < 0:
                    self.x = -self.x
                if int(self.y) < 0:
                    self.y = -self.y
            except:
                pass
            self.ChartProgress.setValue(20)
            #尝试切割
            if "," in self.x:
                self.x_wd = self.x.split(",")
                print(self.x_wd)
            elif " " in self.x:
                self.x_wd = self.x.split(" ")
                print(self.x_wd)
            if "," in self.y:
                self.y_wd = self.y.split(",")
                print(self.y_wd)
            elif " " in self.y:
                self.y_wd = self.y.split(" ")
                print(self.y_wd)
            #判断图表类型
            if index_text == "柱状图/Bar":
                chart = Bar(self.write_lang_ui("柱状图数据"))
            if index_text == "折线图/Line":
                chart = Line(self.write_lang_ui("折线图数据"))
            if index_text == "饼状图/Pie":
                chart = Pie(self.write_lang_ui("饼状图数据"))
            self.ChartProgress.setValue(40)
            #判断切割结果
            try:
                if self.x_wd and not self.y_wd:
                    chart.add(index_text,self.x_wd,self.y)
                    print("x_wd:True y_wd:False")
                elif self.x_wd and self.y_wd:
                    chart.add(index_text,self.x_wd,self.y_wd)
                    print("x_wd:True y_wd:True")
                elif self.y_wd and not self.x_wd:
                    chart.add(index_tex,self.y_wd,self.x)
                    print("x_wd:Flase y_wd:True")
                else:
                    chart.add(index_text,self.y, self.x)
                    print("x_wd:Flase y_wd:False")
                self.ChartProgress.setValue(80)
                chart.render()
                self.ChartProgress.setValue(100)
                ult.ospen("render.html")
            except AssertionError:#项数不一致引起的断言错误
                QMessageBox.warning(self,self.write_lang_ui("注意"),self.write_lang_ui("请确保X轴和Y轴项数一致"))
    def save(self):
        if os.path.exists("render.html"):
            file_path = QFileDialog.getSaveFileName(caption=self.write_lang_ui("保存文件"),filter="(*.html)")
            if file_path[0]:
                save_path = file_path[0]
                shutil.copy("render.html",file_path[0])
                QMessageBox.information(self,write_lang_ui("成功"),write_lang_ui("保存图表成功!"))
            else:
                QMessageBox.warning(self,self.write_lang_ui("注意"),self.write_lang_ui("请重新选择保存位置"))
        else:
            QMessageBox.warning(self,self.write_lang_ui("注意"),self.write_lang_ui("请先进行图表渲染"))
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.get_data()
    def select_lang(self):
        if self.cbox_LangSelect.currentText() == "简体中文":
            self.lang = 0
            print("Setting:Lang:Chinese")
            self.pbtn_render.setText("渲染图表")
            self.pbtn_ok_x.setText("确认")
            self.pbtn_ok_y.setText("确认")
            self.pbtn_OpenData.setText("打开数据")
            self.pbtn_SelectData.setText("保存数据")
        else:
            self.lang = 1
            print("Setting:Lang:English")
            self.pbtn_render.setText("Rend")
            self.pbtn_ok_x.setText("OK")
            self.pbtn_ok_y.setText("OK")
            self.pbtn_OpenData.setText("Open Data")
            self.pbtn_SelectData.setText("Select Data form...")
    def write_lang_ui(self, sent):
        if self.lang == 1:
            if sent == "注意":
                return "Warning"
            if sent == "保存图表成功!":
                return "Saved Chart successful!"
            if sent == "请先进行图表渲染":
                return "Please rend thr chart first!"
            if sent == "成功":
                return "Successful"
            if sent == "请确保X轴和Y轴项数一致":
                return "Please keep X data and Y data in the json file's long is currect."
            if sent == "柱状图数据":
                return "Bar Data Chart"
            if sent == "折线图数据":
                return " Line Data Chart"
            if sent == "饼状图数据":
                return "Pie Data Chart"
            if sent == "使用用户输入的数据":
                return "Using User's input data..."
            if sent == "从文件导入数据":
                return "Select Data File..."
            if sent == "类型":
                return "Type/X"
            if sent == "数据":
                return "Data"
        elif self.lang == 0:
            return sent
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChartWorking()
    sys.exit(app.exec_())
