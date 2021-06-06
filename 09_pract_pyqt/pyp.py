# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:28:43 2021

@author: MAGI
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QLabel
from PyQt5.QtGui import QIcon,QPalette
from PyQt5.QtCore import pyqtSlot,Qt

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = '9 laba'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 140
        self.initUI()
    
    def initUI(self):
        label1=QLabel(self)
        label2=QLabel(self)
                
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Create Label
        label1.setText("<font color=black>First Number</font>")
        label1.move(20, 0)
        label2.setText("<font color=black>Second Number</font>")
        label2.move(150, 0)
            
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(100,40)
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 20)
        self.textbox2.resize(100,40)
        
        
        # Create a button in the window
        self.buttonSum = QPushButton('+', self)
        self.buttonSum.move(20,80)
        self.buttonSum.resize(30,40)
        
        self.buttonMin = QPushButton('-', self)
        self.buttonMin.move(60,80)
        self.buttonMin.resize(30,40)
        
        self.buttonMul = QPushButton('*', self)
        self.buttonMul.move(100,80)
        self.buttonMul.resize(30,40)
        
        self.buttonDiv = QPushButton('/', self)
        self.buttonDiv.move(140,80)
        self.buttonDiv.resize(30,40)
        
        self.buttonSt = QPushButton('^', self)
        self.buttonSt.move(180,80)
        self.buttonSt.resize(30,40)
        
        # connect button to function on_click
        self.buttonSum.clicked.connect(self.on_click_sum)
               
        self.buttonMin.clicked.connect(self.on_click_min)
               
        self.buttonMul.clicked.connect(self.on_click_mul)
               
        self.buttonDiv.clicked.connect(self.on_click_div)
                
        self.buttonSt.clicked.connect(self.on_click_step)
        self.show()
        
       
    
    @pyqtSlot()
    def on_click_sum(self):
        textboxValue1 = self.textbox.text()
        textboxValue2 = self.textbox2.text()
        value1=int(textboxValue1)
        value2=int(textboxValue2)
        ans=str(value1+value2)
        print(value1)
        print(value2)
        
        QMessageBox.question(self, 'Ans ', "Sum= " + ans, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        
    @pyqtSlot()
    def on_click_min(self):
        textboxValue1 = self.textbox.text()
        textboxValue2 = self.textbox2.text()
        value1=int(textboxValue1)
        value2=int(textboxValue2)
        ans=str(value1-value2)
        print(value1)
        print(value2)
        
        QMessageBox.question(self, 'Ans ', "Min= " + ans, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    @pyqtSlot()
    def on_click_mul(self):
        textboxValue1 = self.textbox.text()
        textboxValue2 = self.textbox2.text()
        value1=int(textboxValue1)
        value2=int(textboxValue2)
        ans=str(value1*value2)
        print(value1)
        print(value2)
        
        QMessageBox.question(self, 'Ans ', "Mul= " + ans, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    @pyqtSlot()
    def on_click_div(self):
        textboxValue1 = self.textbox.text()
        textboxValue2 = self.textbox2.text()
        value1=float(textboxValue1)
        value2=float(textboxValue2)
        ans=str(value1/value2)
        print(value1)
        print(value2)
        
        QMessageBox.question(self, 'Ans ', "Div= " + ans, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    @pyqtSlot()
    def on_click_step(self):
        textboxValue1 = self.textbox.text()
        textboxValue2 = self.textbox2.text()
        value1=int(textboxValue1)
        value2=int(textboxValue2)
        ans=str(value1**value2)
        print(value1)
        print(value2)
        
        QMessageBox.question(self, 'Ans ', "Step= " + ans, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())