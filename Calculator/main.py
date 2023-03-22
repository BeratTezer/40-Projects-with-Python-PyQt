from CalculatorUI import Ui_MainWindow
from PyQt6 import QtCore
from PyQt6 import QtWidgets
import sys

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # Variables
        self.screenText = ""
        self.calculation = 0
        
        # Configurations
        self.ui.screenLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignCenter)
    
        # Connections between buttons and functions
        # self.ui.zeroButton.clicked.connect()
        # self.ui.oneButton.clicked.connect()
        # self.ui.twoButton.clicked.connect()
        # self.ui.threeButton.clicked.connect()
        # self.ui.fourButton.clicked.connect()
        # self.ui.fiveButton.clicked.connect()
        # self.ui.sixButton.clicked.connect()
        # self.ui.sevenButton.clicked.connect()
        # self.ui.eightButton.clicked.connect()
        # self.ui.nineButton.clicked.connect()
        # self.ui.backspaceButton.clicked.connect()
        # self.ui.multiplyButton.clicked.connect()
        # self.ui.divideButton.clicked.connect()
        # self.ui.plusButton.clicked.connect()
        # self.ui.minusButton.clicked.connect()
        # self.ui.percentButton.clicked.connect()
        # self.ui.commaButton.clicked.connect()
        
        self.ui.equalButton.clicked.connect(self.printScreen)
        # self.ui.equalButton.clicked.connect(self.equal(self.screenText, 0))
    
    # Functions
    def equal(self, text, i):
        # Recursion
        # if type(text.split(" ")[0]) == 
        pass
    
    def printScreen(self, input):
        if (len(self.screenText) == 0):
            if (int(input) not in range(10)):
                self.screenText += str(input)
        self.ui.screenLabel.setText(self.screenText)
    
    def collect(self):
        pass
    
    def extraction(self):
        pass
    
    def multiply(self):
        pass
    
    def divide(self):
        pass
    
    def mod(self):
        pass
    
    def clean(self):
        pass
    
    def erase(self):
        pass
    
    


def CalculatorWindow():
    CalculatorWindow = QtWidgets.QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(CalculatorWindow.exec())
    
CalculatorWindow()