from Ui_mainwindow import Ui_MainWindow
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PIL import Image, ImageGrab,ImageQt
import pyperclip
import time 
import os

class Mymainwindow(Ui_MainWindow):
    def __init__(self, mainwindow):
        super().setupUi(mainwindow)
        self.splt = '/'
        self.imgformat = '.png'
        self.imgname = ''
        self.predix = ''
        self.rootPath = '.'
        self.lastsave = ''
        self.timer = QTimer(mainwindow)
        self.timer.timeout.connect(self.getImage)
        self.timer.start(500)
        self.mainwindow = mainwindow
        
        self.radioButton.toggled.connect(self.seltype)
        self.radioButton.setChecked(True)
        self.type = self.radioButton.text()
        self.radioButton_2.toggled.connect(self.seltype)
        self.radioButton_3.toggled.connect(self.seltype)
        self.radioButton_4.toggled.connect(self.seltype)
        self.radioButton_5.toggled.connect(self.seltype)
        self.radioButton_6.toggled.connect(self.seltype)
        self.radioButton_7.toggled.connect(self.seltype)
        self.radioButton_8.toggled.connect(self.seltype)
        self.radioButton_9.toggled.connect(self.seltype)
        self.radioButton_10.toggled.connect(self.seltype)
        self.radioButton_11.toggled.connect(self.seltype)
        self.radioButton_12.toggled.connect(self.seltype)
        self.radioButton_13.toggled.connect(self.seltype)
        self.radioButton_14.toggled.connect(self.seltype)
        self.radioButton_15.toggled.connect(self.seltype)
        self.radioButton_16.toggled.connect(self.seltype)
        self.radioButton_17.toggled.connect(self.seltype)

        self.saveButton.clicked.connect(self.saveImg)
        self.selpathButton.clicked.connect(self.selPath)
        self.dellastButton.clicked.connect(self.dellast)
        self.dellastButton.setEnabled(False)
        self.checkBox.setChecked(False)
        self.saveButton.setEnabled(False)


    def dellast(self):
        if os.path.exists(self.lastsave):
            os.remove(self.lastsave)
        self.label.clear()
        self.dellastButton.setEnabled(False)
        self.pathEdit.setText('')

    def selPath(self):
        self.rootPath = QFileDialog.getExistingDirectory(self.mainwindow, '选择文件夹')
        self.savefolderPath = self.rootPath + self.splt + self.type
        self.savePath = self.savefolderPath + self.splt +self.imgname
        self.pathEdit.setText(self.savePath)

    def saveImg(self):
        if not os.path.exists(self.savefolderPath):
            os.makedirs(self.savefolderPath)
        self.pilimg.save(self.savePath)
        self.lastsave = self.savePath
        self.minimized()
        self.dellastButton.setEnabled(True)
        self.saveButton.setEnabled(False)

    def seltype(self):
        typebutton = self.mainwindow.sender()
        self.type = typebutton.text()
        self.savefolderPath = self.rootPath + self.splt + self.type 
        self.imgname = self.predix+'-'+self.type+'-'+'_'.join(str(time.time()).split('.')) + self.imgformat
        self.savePath = self.savefolderPath + self.splt + self.imgname
        self.pathEdit.setText(self.savePath)

    def minimized(self):
        self.mainwindow.showMinimized()

    def normalized(self):
        self.mainwindow.showNormal()

    def getImage(self):
        im = ImageGrab.grabclipboard()
        if isinstance(im, Image.Image):
            pyperclip.copy('')
            self.pilimg = im
            self.normalized()
            self.img = ImageQt.ImageQt(im)
            self.label.setPixmap(QPixmap.fromImage(self.img.scaled(291,301, Qt.KeepAspectRatio)))
            self.predix = time.strftime("%Y%m%d", time.localtime())
            self.imgname = self.predix+'-'+self.type+'-'+'_'.join(str(time.time()).split('.')) + self.imgformat
            self.savePath = self.savefolderPath + self.splt + self.imgname
            self.pathEdit.setText(self.savePath)
            self.saveButton.setEnabled(True)
            if self.checkBox.isChecked():
                self.saveImg()
            # self.textBrowser.
        else:
            pass