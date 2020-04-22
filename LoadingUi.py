# these are the necessary commands for loading a UI 
import sys
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('yourUI.ui', self) # Load the .ui file
        self.show() # Show the GUI



        



app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # 
