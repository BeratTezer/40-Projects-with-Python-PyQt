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
        self.screenText = " "
        self.calculation = 0
        
        # Configurations
        self.ui.screenLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignCenter)
    
        # Connections between buttons and functions
        self.ui.zeroButton.clicked.connect(lambda: self.printScreen("0"))
        self.ui.oneButton.clicked.connect(lambda: self.printScreen("1"))
        self.ui.twoButton.clicked.connect(lambda: self.printScreen("2"))
        self.ui.threeButton.clicked.connect(lambda: self.printScreen("3"))
        self.ui.fourButton.clicked.connect(lambda: self.printScreen("4"))
        self.ui.fiveButton.clicked.connect(lambda: self.printScreen("5"))
        self.ui.sixButton.clicked.connect(lambda: self.printScreen("6"))
        self.ui.sevenButton.clicked.connect(lambda: self.printScreen("7"))
        self.ui.eightButton.clicked.connect(lambda: self.printScreen("8"))
        self.ui.nineButton.clicked.connect(lambda: self.printScreen("9"))
        self.ui.backspaceButton.clicked.connect(lambda: self.printScreen("#"))
        self.ui.multiplyButton.clicked.connect(lambda: self.printScreen(" * "))
        self.ui.divideButton.clicked.connect(lambda: self.printScreen(" / "))
        self.ui.plusButton.clicked.connect(lambda: self.printScreen(" + "))
        self.ui.minusButton.clicked.connect(lambda: self.printScreen(" - "))
        self.ui.percentButton.clicked.connect(lambda: self.printScreen(" % "))
        self.ui.commaButton.clicked.connect(lambda: self.printScreen(","))
        
        # self.ui.equalButton.clicked.connect(self.printScreen)
        # self.ui.equalButton.clicked.connect(self.equal(self.screenText, 0))
    
    # Functions
    def equal(self, text, i):
        # Recursion
        # if type(text.split(" ")[0]) == 
        pass
    
    def printScreen(self, input):
        cont = 0
        if len(input) == 3 and len(self.screenText) == 1:
            if input in [" * ", " - ", " + ", " / ", " % "]:
                cont = 1
        if input == "," and list(self.screenText)[-1] == " ":
            input = "0,"
        if input in [" * ", " - ", " + ", " / ", " % "] and list(self.screenText)[-1] == " ":
            cont = 1
        if cont == 0:
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