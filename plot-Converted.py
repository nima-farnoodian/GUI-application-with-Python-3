# -*- coding: utf-8 -*-

# Author: Nima Farnoodian- nima.farnoodian@acm.org/ nima.farnoodian@outlook.com

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 358)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(415, 358))
        MainWindow.setMaximumSize(QtCore.QSize(415, 358))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.groupBox.setObjectName("groupBox")
        self.start = QtWidgets.QLineEdit(self.groupBox)
        self.start.setGeometry(QtCore.QRect(30, 20, 91, 20))
        self.start.setText("")
        self.start.setObjectName("start")
        self.end = QtWidgets.QLineEdit(self.groupBox)
        self.end.setGeometry(QtCore.QRect(160, 20, 101, 20))
        self.end.setText("")
        self.end.setObjectName("end")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(-30, 40, 851, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../NewSeek/newseek4.jpg"))
        self.label.setObjectName("label")
        self.Generate = QtWidgets.QPushButton(self.groupBox)
        self.Generate.setGeometry(QtCore.QRect(300, 10, 91, 31))
        self.Generate.setObjectName("Generate")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 35, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 35, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 391, 221))
        self.listWidget.setObjectName("listWidget")
        self.Plot = QtWidgets.QPushButton(self.centralwidget)
        self.Plot.setGeometry(QtCore.QRect(320, 286, 91, 31))
        self.Plot.setObjectName("Plot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Plot.setDisabled(True)

        self.Generate.clicked.connect(self.numbergenerator)
        self.Plot.clicked.connect(self.plotting)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plot"))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.Generate.setText(_translate("MainWindow", "Generate"))
        self.label_2.setText(_translate("MainWindow", "X:"))
        self.label_3.setText(_translate("MainWindow", "Y:"))
        self.Plot.setText(_translate("MainWindow", "Plot"))
    def numbergenerator(self):
        x=int(self.start.text())
        y=int(self.end.text())
        self.numbers=np.linspace(x,y,50)
        self.Ncos=np.cos(self.numbers)
        self.Nsin=np.sin(self.numbers)
        self.listWidget.addItem('Number\tCos\tSin')
        for i in range( len(self.numbers)):
            printTxt= str(self.numbers[i])+'\t' +str(self.Ncos[i])+ '\t'+str(self.Nsin[i])
            self.listWidget.addItem(printTxt)
        self.Plot.setEnabled(True)

    def plotting(self):
        NumberPlot=plt.figure('Plotting Cos and Sin')
        NumberPlot.clear()
        plt.plot(self.numbers,self.Ncos,label='Cos')
        plt.plot(self.numbers,self.Nsin,label='Sin')
        plt.legend(loc='best')
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
