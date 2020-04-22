# Author: Nima Farnoodian- nima.farnoodian@acm.org/ nima.farnoodian@outlook.com

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import  QMessageBox
import matplotlib.pyplot as plt
import numpy as np
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('plot.ui', self) # Load the .ui file
        self.show() # Show the GUI

        # to connecet each widget to an object in python. Each object (variables) refers to the widget it is linked to.
        self.Generate_btn = self.findChild(QtWidgets.QPushButton, 'Generate') 
        self.Plot_btn = self.findChild(QtWidgets.QPushButton, 'Plot') 
        self.display_list=self.findChild(QtWidgets.QListWidget, 'listWidget')
        
        self.Plot_btn.setEnabled(False)
        # to connecet the buttons to their functions
        self.Generate_btn.clicked.connect(self.numbergenerator)
        self.Plot_btn.clicked.connect(self.plotting)

    def numbergenerator(self):
        x=int(self.start.text())
        y=int(self.end.text())
        self.numbers=np.linspace(x,y,50)
        self.Ncos=np.cos(self.numbers)
        self.Nsin=np.sin(self.numbers)
        self.display_list.addItem('Number\tCos\tSin')
        for i in range( len(self.numbers)):
            printTxt= str(self.numbers[i])+'\t' +str(self.Ncos[i])+ '\t'+str(self.Nsin[i])
            self.display_list.addItem(printTxt)
        self.Plot_btn.setEnabled(True)

    def plotting(self):
        msg=QMessageBox()
        msg.setWindowTitle('Question')
        msg.setText('Do you want to generate plot?')     
        msg.setIcon(QMessageBox.Question) 
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes) 
        msg.buttonClicked.connect(self.msgAnswwer)
        msg.exec_()   
       
    
    def msgAnswwer(self,i):
        if i.text()=='&Yes':
            NumberPlot=plt.figure('Plotting Cos and Sin')
            NumberPlot.clear()
            plt.plot(self.numbers,self.Ncos,label='Cos')
            plt.plot(self.numbers,self.Nsin,label='Sin')
            plt.legend(loc='best')
            plt.show()

        else:
            msg2=QMessageBox()
            msg2.setWindowTitle('No plotting')
            msg2.setText('You have decided not to plot')
            msg2.setIcon(QMessageBox.Information)
            msg2.setStandardButtons(QMessageBox.Ok)
            msg2.exec_()
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # 
