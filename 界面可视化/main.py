# -*- coding: utf-8 -*-
from MAT import Ui_MainWindow  # 导入uitestPyQt5.ui转换为uitestPyQt5.py中的类
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QFileDialog,QInputDialog
import cv2
import sys
import numpy as np

#用cv2打开一个窗口，读入并显示一个本地图像文件
cv2.namedWindow('MAT',0)
cv2.resizeWindow('MAT',480,360)
img=cv2.imread('C://Users//EDZ//Pictures//Saved Pictures//girl.jpg')
cv2.imshow('MAT',img)

#这是固定模板，无需更改，如果建立的是QWidget窗口，相应替代即可
class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # class myform(QWidget,Ui_Form):如建立的是Widget项目，导入的是QWidget
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
#####################################主函数代码#################
    def btn_ShowURL(self):
        filename=self.plainTextEdit.toPlainText()
        ret,img=cv2.VideoCapture(filename).read()
        cv2.imshow('MAT',img)

    #按钮按下时，弹出一个对话框，选择一个将要显示的本地图片文件，点击ok，则图片显示在lable中
    def btn_OpenFile(self):
        filename = QFileDialog.getOpenFileName(self,'.jpg','c:')
        self.label.setPixmap(QtGui.QPixmap(filename[0]))

    #EditText文本框中内容按照要求重新赋值
    def btn_Change(self):
        self.textEdit.setText('Timing开挂从这里开始')

    def btn_Dialog(self):
        url, ok = QInputDialog.getText(self, "Input Dialog", "键入网络地址:")
        if ok:
            cap=cv2.VideoCapture(url)
            ret, img=cap.read()
            #cv2.imshow('MAT',img)
            self.label.setPixmap(QPixmap.fromImage(cvMatToQimg(img)))

#按钮按下时，弹出一个对话框，要求键入一个网络地址，点击ok后，lable中显示出来
def cvMatToQimg(mat):
    mat = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
    #mat=cv2.cvtColor(mat,cv2.COLOR_BGR2HSV)
    #mat = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
    return QImage(mat.tostring(), mat.shape[1], mat.shape[0], mat.shape[2] * mat.shape[1], QtGui.QImage.Format_RGB888)

app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
# window=myform()   #如果是QWidget
#windows.show()
#app.exec_()
sys.exit(app.exec_())