# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
""" 2021年2月11日"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 796)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1130, 780))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 60, 390, 680))
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 190, 321, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 250, 211, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_commit_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_commit_1.setObjectName("pushButton_commit_1")
        self.horizontalLayout_3.addWidget(self.pushButton_commit_1)
        self.pushButton_cancel_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_cancel_1.setObjectName("pushButton_cancel_1")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel_1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 40, 301, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.pushButton_Filechoose = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_Filechoose.setObjectName("pushButton_Filechoose")
        self.horizontalLayout_4.addWidget(self.pushButton_Filechoose)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 120, 321, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_5.addWidget(self.spinBox_2)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(80, 260, 211, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_commit_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_commit_2.setObjectName("pushButton_commit_2")
        self.horizontalLayout_6.addWidget(self.pushButton_commit_2)
        self.pushButton_cancel_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_cancel_2.setObjectName("pushButton_cancel_2")
        self.horizontalLayout_6.addWidget(self.pushButton_cancel_2)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 41))
        self.label.setObjectName("label")
        self.label_pic_left = QtWidgets.QLabel(self.tab)
        self.label_pic_left.setGeometry(QtCore.QRect(420, 110, 310, 310))
        self.label_pic_left.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pic_left.setText("")
        self.label_pic_left.setObjectName("label_pic_left")
        self.label_pic_right = QtWidgets.QLabel(self.tab)
        self.label_pic_right.setGeometry(QtCore.QRect(790, 110, 310, 310))
        self.label_pic_right.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pic_right.setText("")
        self.label_pic_right.setObjectName("label_pic_right")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(740, 240, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(520, 500, 470, 140))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(410, 90, 330, 340))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(780, 90, 330, 340))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(510, 470, 491, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_left = QtWidgets.QComboBox(self.tab)
        self.comboBox_left.setGeometry(QtCore.QRect(470, 50, 211, 22))
        self.comboBox_left.setObjectName("comboBox_left")
        self.comboBox_right = QtWidgets.QComboBox(self.tab)
        self.comboBox_right.setGeometry(QtCore.QRect(840, 50, 211, 22))
        self.comboBox_right.setObjectName("comboBox_right")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 9, 720, 730))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.tabWidget_2.raise_()
        self.label.raise_()
        self.label_pic_left.raise_()
        self.label_pic_right.raise_()
        self.label_5.raise_()
        self.textBrowser.raise_()
        self.comboBox_left.raise_()
        self.comboBox_right.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 40, 271, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.pushButton_Imagechoose = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_Imagechoose.setObjectName("pushButton_Imagechoose")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_Imagechoose)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_9)
        self.toolBox = QtWidgets.QToolBox(self.formLayoutWidget)
        self.toolBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 269, 99))
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(2, 0, 251, 61))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_7)
        self.spinBox_3.setMinimum(2)
        self.spinBox_3.setMaximum(999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_9.addWidget(self.spinBox_3)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 269, 99))
        self.page_2.setObjectName("page_2")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 72, 15))
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.spinBox_4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_8)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_10.addWidget(self.spinBox_4)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(130, 20, 111, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.spinBox_5 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_9)
        self.spinBox_5.setMinimum(2)
        self.spinBox_5.setMaximum(9999)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_11.addWidget(self.spinBox_5)
        self.toolBox.addItem(self.page_2, "")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.toolBox)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setSingleStep(0.001)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(60, 280, 211, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_commit_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_commit_3.setObjectName("pushButton_commit_3")
        self.horizontalLayout_7.addWidget(self.pushButton_commit_3)
        self.pushButton_cancel_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_cancel_3.setObjectName("pushButton_cancel_3")
        self.horizontalLayout_7.addWidget(self.pushButton_cancel_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 350, 311, 321))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_pic_left_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_pic_left_2.setGeometry(QtCore.QRect(10, 20, 291, 291))
        self.label_pic_left_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pic_left_2.setText("")
        self.label_pic_left_2.setObjectName("label_pic_left_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(330, 0, 791, 741))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 581, 641))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget.setGeometry(QtCore.QRect(600, 50, 181, 641))
        self.listWidget.setObjectName("listWidget")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(90, 670, 151, 20))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.groupBox_6.raise_()
        self.groupBox_5.raise_()
        self.formLayoutWidget.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.label_13.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于语义匹配的图像检索系统"))
        self.label_2.setText(_translate("MainWindow", "参与匹配图像数量："))
        self.pushButton_commit_1.setText(_translate("MainWindow", "确定"))
        self.pushButton_cancel_1.setText(_translate("MainWindow", "取消"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "随机选择"))
        self.label_3.setText(_translate("MainWindow", "选择起始图像："))
        self.pushButton_Filechoose.setText(_translate("MainWindow", "选择文件"))
        self.label_4.setText(_translate("MainWindow", "参与匹配图像数量："))
        self.pushButton_commit_2.setText(_translate("MainWindow", "确定"))
        self.pushButton_cancel_2.setText(_translate("MainWindow", "取消"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "定向选择"))
        self.label.setText(_translate("MainWindow", "相似度计算两种图像选择方式如下："))
        self.label_5.setText(_translate("MainWindow", "VS"))
        self.groupBox.setTitle(_translate("MainWindow", "图像"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图像"))
        self.groupBox_3.setTitle(_translate("MainWindow", "图像相似度"))
        self.groupBox_4.setTitle(_translate("MainWindow", "图像及相似度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "相似度计算"))
        self.label_6.setText(_translate("MainWindow", "选择图像："))
        self.pushButton_Imagechoose.setText(_translate("MainWindow", "选择图像"))
        self.label_9.setText(_translate("MainWindow", "选择匹配方式："))
        self.label_7.setText(_translate("MainWindow", "参与匹配的图像数量："))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "随机选择"))
        self.label_10.setText(_translate("MainWindow", "选择范围："))
        self.label_11.setText(_translate("MainWindow", "from"))
        self.label_12.setText(_translate("MainWindow", "to"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "定向选择"))
        self.label_8.setText(_translate("MainWindow", "阈值："))
        self.pushButton_commit_3.setText(_translate("MainWindow", "确定"))
        self.pushButton_cancel_3.setText(_translate("MainWindow", "取消"))
        self.groupBox_5.setTitle(_translate("MainWindow", "图像"))
        self.groupBox_6.setTitle(_translate("MainWindow", "匹配图像"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图像匹配"))
