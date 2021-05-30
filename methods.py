import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Frame import Ui_MainWindow
import data_choose
import data_choose2
import readxml
import WordNet
import numpy as np
""" 2021年3月12日"""

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.qw = QWidget()
        self.setupUi(self)
        self.pushButton_commit_1.clicked.connect(self.CalculateandDisplay)
        self.pushButton_cancel_1.clicked.connect(self.cancelClear)
        self.pushButton_commit_2.clicked.connect(self.CalculateandDisplay)
        self.pushButton_cancel_2.clicked.connect(self.cancelClear)
        self.pushButton_Filechoose.clicked.connect(self.chooseFile)
        self.pushButton_Imagechoose.clicked.connect(self.chooseFile)
        self.pushButton_commit_3.clicked.connect(self.matchImage)
        self.pushButton_cancel_3.clicked.connect(self.clearMatch)
        self.listWidget.itemClicked.connect(self.displayMatchImage)

    # 随机选择
    def randomChoose(self, random):
        if random != 0:
            rd = random
            dc1 = data_choose.data_choose()
            list1 = dc1.Random_choose(rd)
            return list1

    # 定向选择
    def orientChoose(self, orient1, orient2):
        if orient1 and orient2:
            dc2 = data_choose2.data_choose2()
            list2 = dc2.Orientation_choose(orient1, orient2)
            return list2

    # 计算相似度并显示
    def CalculateandDisplay(self):
        sender = self.sender()
        if sender.objectName() == 'pushButton_commit_1':
            random = self.spinBox.value()
            list1 = self.randomChoose(random)
            self.showIndex_ran(list1)
            self.similarity()
        elif sender.objectName() == 'pushButton_commit_2':
            # 此处应将or1 修改为选择图片对应的xml文件的位置
            pos = self.getPicturePosition()
            orient1 = pos - 1
            orient2 = self.spinBox_2.value()
            list2 = self.orientChoose(orient1, orient2)
            self.showIndex_ori(list2)
            self.similarity()

    # 相似度计算
    def similarity(self):
        rdx = readxml.readxml()
        wn2 = WordNet.WordNet()
        self.comboBox_left.currentIndexChanged.connect(self.similarity)
        self.comboBox_right.currentIndexChanged.connect(self.similarity)
        self.textBrowser.clear()
        name1 = self.comboBox_left.currentText()
        name2 = self.comboBox_right.currentText()
        picname1 = name1.replace('.jpg', '.xml')
        picname2 = name2.replace('.jpg', '.xml')
        arr1 = np.array(rdx.readxml(picname1))
        arr2 = np.array(rdx.readxml(picname2))
        str1 = ' '.join(arr1)
        str2 = ' '.join(arr2)
        print(str1, str2)
        list_wn = str(wn2.similarity(str1, str2))
        print("Similarity of " + name1 + " and " + name2 + " is: " + list_wn + "\n")
        self.textBrowser.append(
            "Similarity of " + name1 + " and " + name2 + " is: " + list_wn + "\n")

    # 随机选择 显示选中的文件列表
    def showIndex_ran(self, list):
        self.comboboxClearandChange()
        self.textBrowser.clear()
        for i in list:
            print("随机选择的文件是：" + i)
            j = i.replace('.xml', '.jpg')
            self.comboBox_left.addItem(j)
            self.comboBox_right.addItem(j)

    # 定向选择 显示选中的文件列表
    def showIndex_ori(self, list):
        self.comboboxClearandChange_Right()
        self.textBrowser.clear()
        for i in list:
            print("选择的文件是：" + i)
            j = i.replace('.xml', '.jpg')
            self.comboBox_right.addItem(j)

    # 获取文件绝对路径
    def readfile(self, str):
        path = os.getcwd()  # 获取程序所在文件夹路径
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if filename == str:
                    # print(os.path.join(dirpath, filename))
                    return os.path.join(dirpath, filename)

    # 随机选择 在label标签显示图片
    def displayImage(self, name1, name2):
        image_left = QtGui.QPixmap(self.readfile(name1)).scaled(self.label_pic_left.width(),
                                                                self.label_pic_left.height())
        self.label_pic_left.setPixmap(image_left)
        image_right = QtGui.QPixmap(self.readfile(name2)).scaled(self.label_pic_right.width(),
                                                                 self.label_pic_right.height())
        self.label_pic_right.setPixmap(image_right)

    # 定向选择 在左label标签显示图片
    def displayImageLeft(self, name):
        image_left = QtGui.QPixmap(self.readfile(name)).scaled(self.label_pic_left.width(),
                                                               self.label_pic_left.height())
        self.label_pic_left.setPixmap(image_left)

    # 定向选择 在右label标签显示图片
    def displayImageRight(self, name):
        image_right = QtGui.QPixmap(self.readfile(name)).scaled(self.label_pic_right.width(),
                                                                self.label_pic_right.height())
        self.label_pic_right.setPixmap(image_right)

    # 下拉选择改变
    def selectionChange(self):
        name1 = self.comboBox_left.currentText()
        name2 = self.comboBox_right.currentText()
        self.displayImage(name1, name2)

    # 右下拉选择改变
    def selectionChangeRight(self):
        name = self.comboBox_right.currentText()
        self.displayImageRight(name)

    # 图像选择
    def chooseFile(self):
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;JPG Files(*.jpg);;PNG Files(*.png)")
        print(filename)
        if filename != "":
            # return filename
            name = self.getPictureName(filename)
            sender = self.sender()
            if sender.text() == '选择文件':
                self.cancelClear()
                self.comboBox_left.addItem(name)
                self.displayImageLeft(name)
            elif sender.text() == '选择图像':
                self.displayImage_match(name)
                self.label_13.setText(name)
        else:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '请选择图像！')
            msg_box.exec_()

    # 获取图像名称
    def getPictureName(self, imageName):
        filename = imageName
        pathname = filename.split('/')  # 将文件路径按/切分
        # pathx = "/".join(pathname[0:len(pathname)-1]) #假设切分后有n部分，前n-1部分用/重新拼接即为文件路径
        namex = pathname[len(pathname) - 1]
        return namex

    # 获取选择图像在图库中的位置
    def getPicturePosition(self):
        picname = self.comboBox_left.currentText()
        picpath = self.readfile(picname).split('\\')
        path = '/'.join((picpath[0:len(picpath) - 1]))
        list = os.listdir(path)
        for i in range(0, len(list)):
            if list[i] == self.comboBox_left.currentText():
                print(i)
                return i

    # 取消按钮清空
    def cancelClear(self):
        self.comboboxClearandChange()
        self.label_pic_left.clear()
        self.label_pic_right.clear()
        self.textBrowser.clear()

    # combobox内容选择及清空
    def comboboxClearandChange(self):
        self.comboBox_left.disconnect()
        self.comboBox_right.disconnect()
        self.comboBox_left.clear()
        self.comboBox_right.clear()
        self.comboBox_left.currentIndexChanged.connect(self.selectionChange)
        self.comboBox_right.currentIndexChanged.connect(self.selectionChange)

    # 定向选择 combobox内容选择及清空
    def comboboxClearandChange_Right(self):
        self.comboBox_right.disconnect()
        self.comboBox_right.clear()
        self.comboBox_right.currentIndexChanged.connect(self.selectionChangeRight)

    # 图像匹配 label左2显示图像
    def displayImage_match(self, name):
        image = QtGui.QPixmap(self.readfile(name)).scaled(self.label_pic_left_2.width(),
                                                          self.label_pic_left_2.height())
        self.label_pic_left_2.setPixmap(image)

    # 图像匹配 相似度计算
    def similarity_match(self, name1, name2):
        rdx = readxml.readxml()
        wn = WordNet.WordNet()
        picname1 = name1.replace('.jpg', '.xml')
        picname2 = name2
        arr1 = np.array(rdx.readxml(picname1))
        arr2 = np.array(rdx.readxml(picname2))
        str1 = ' '.join(arr1)
        str2 = ' '.join(arr2)
        print(str1, str2)
        list_wn = str(wn.similarity(str1, str2))
        print("Similarity of " + picname1 + " and " + name2 + " is: " + list_wn + "\n")
        return list_wn

    # 图像匹配
    def matchImage(self):
        # 指定的阈值
        threshold = self.doubleSpinBox.value()
        random = self.spinBox_3.value()
        orient_first = self.spinBox_4.value() - 2
        orient_last = self.spinBox_5.value() - 2
        amount = orient_last - orient_first + 1
        name_choose = self.label_13.text()
        if self.toolBox.currentIndex() == 0:
            list1 = self.randomChoose(random)
            print(list1)
            list_name_1 = list1[:]
            for i in range(0, len(list1)):
                list_wn_1 = self.similarity_match(name_choose, list1[i])
                if float(list_wn_1) >= threshold:
                    print(list_wn_1)
                    # self.label_sim.setText('与选中图像的相似度为:'+list_wn_1)
                    self.displayNameList(list_name_1)
                else:
                    list_name_1.remove(list1[i])
                    print(list_name_1)
                    self.displayNameList(list_name_1)
                    if not list_name_1:
                        msg_box = QMessageBox(QMessageBox.Warning, 'Result', '无匹配图像，请修改数据或重新选择图像！')
                        msg_box.exec_()
        elif self.toolBox.currentIndex() == 1 and orient_first < orient_last:
            list2 = self.orientChoose(orient_first, amount)
            print(list2)
            list_name_2 = list2[:]
            for i in range(0, len(list2)):
                list_wn_2 = self.similarity_match(name_choose, list2[i])
                if float(list_wn_2) >= threshold:
                    print(list_wn_2)
                    self.displayNameList(list_name_2)
                else:
                    list_name_2.remove(list2[i])
                    print(list_name_2)
                    self.displayNameList(list_name_2)
                    if not list_name_2:
                        msg_box = QMessageBox(QMessageBox.Warning, 'Result', '无匹配图像，请修改数据或重新选择图像！')
                        msg_box.exec_()

    # 滚动显示匹配的图像
    def displayNameList(self, name_list):
        self.listWidget.clear()
        self.label_14.clear()
        for i in name_list:
            j = i.replace('.xml', '.jpg')
            self.listWidget.addItem(j)

    # 点击列表中选项后显示图像
    def displayMatchImage(self, item):
        imagename = item.text()
        image = QtGui.QPixmap(self.readfile(imagename)).scaled(self.label_14.width(), self.label_14.height())
        self.label_14.setPixmap(image)

    # 图像匹配点击取消清空
    def clearMatch(self):
        self.listWidget.clear()
        self.label_14.clear()
        self.label_pic_left_2.clear()
        self.label_13.clear()



