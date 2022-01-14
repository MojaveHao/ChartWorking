# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChartWorkingWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 266)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_x = QLabel(self.centralwidget)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setGeometry(QRect(80, 80, 47, 14))
        self.label_y = QLabel(self.centralwidget)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(80, 120, 47, 14))
        self.ChartProgress = QProgressBar(self.centralwidget)
        self.ChartProgress.setObjectName(u"ChartProgress")
        self.ChartProgress.setGeometry(QRect(70, 160, 381, 23))
        self.ChartProgress.setValue(0)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 190, 531, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pbtn_render = QPushButton(self.horizontalLayoutWidget)
        self.pbtn_render.setObjectName(u"pbtn_render")

        self.horizontalLayout.addWidget(self.pbtn_render)

        self.pbtn_SelectData = QPushButton(self.horizontalLayoutWidget)
        self.pbtn_SelectData.setObjectName(u"pbtn_SelectData")

        self.horizontalLayout.addWidget(self.pbtn_SelectData)

        self.pbtn_OpenData = QPushButton(self.horizontalLayoutWidget)
        self.pbtn_OpenData.setObjectName(u"pbtn_OpenData")

        self.horizontalLayout.addWidget(self.pbtn_OpenData)

        self.cbox_Type = QComboBox(self.horizontalLayoutWidget)
        self.cbox_Type.addItem("")
        self.cbox_Type.addItem("")
        self.cbox_Type.addItem("")
        self.cbox_Type.addItem("")
        self.cbox_Type.setObjectName(u"cbox_Type")

        self.horizontalLayout.addWidget(self.cbox_Type)

        self.cbox_LangSelect = QComboBox(self.horizontalLayoutWidget)
        self.cbox_LangSelect.addItem("")
        self.cbox_LangSelect.addItem("")
        self.cbox_LangSelect.setObjectName(u"cbox_LangSelect")

        self.horizontalLayout.addWidget(self.cbox_LangSelect)

        self.pbtn_oklang = QPushButton(self.horizontalLayoutWidget)
        self.pbtn_oklang.setObjectName(u"pbtn_oklang")

        self.horizontalLayout.addWidget(self.pbtn_oklang)

        self.ledit_x = QLineEdit(self.centralwidget)
        self.ledit_x.setObjectName(u"ledit_x")
        self.ledit_x.setGeometry(QRect(130, 80, 251, 21))
        self.ledit_y = QLineEdit(self.centralwidget)
        self.ledit_y.setObjectName(u"ledit_y")
        self.ledit_y.setGeometry(QRect(130, 120, 251, 21))
        self.pbtn_ok_x = QPushButton(self.centralwidget)
        self.pbtn_ok_x.setObjectName(u"pbtn_ok_x")
        self.pbtn_ok_x.setGeometry(QRect(390, 80, 41, 22))
        self.pbtn_ok_y = QPushButton(self.centralwidget)
        self.pbtn_ok_y.setObjectName(u"pbtn_ok_y")
        self.pbtn_ok_y.setGeometry(QRect(390, 120, 41, 22))
        self.pbtn_ver = QPushButton(self.centralwidget)
        self.pbtn_ver.setObjectName(u"pbtn_ver")
        self.pbtn_ver.setGeometry(QRect(-10, 220, 581, 22))
        self.lb_title = QLabel(self.centralwidget)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setGeometry(QRect(130, 20, 401, 51))
        font = QFont()
        font.setPointSize(16)
        self.lb_title.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pbtn_render.setText(QCoreApplication.translate("MainWindow", u"\u6e32\u67d3\u56fe\u8868", None))
        self.pbtn_SelectData.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.pbtn_OpenData.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6570\u636e", None))
        self.cbox_Type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u997c\u72b6\u56fe/Pie", None))
        self.cbox_Type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u67f1\u72b6\u56fe/Bar", None))
        self.cbox_Type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6298\u7ebf\u56fe/Line", None))
        self.cbox_Type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u66f4\u591a\u6b63\u5728\u5f00\u53d1\u4e2d", None))

        self.cbox_LangSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.cbox_LangSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.pbtn_oklang.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u8bed\u8a00", None))
        self.pbtn_ok_x.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.pbtn_ok_y.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.pbtn_ver.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a1.0.0                 \u5236\u4f5c\u8005\uff1aMojaveHao", None))
        self.lb_title.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u8868\u751f\u6210\u5668   ChartWorking", None))
    # retranslateUi

