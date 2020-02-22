from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout, QLineEdit, QLabel,QPushButton
import sys
from os import listdir
from os.path import isfile, join
import re
import numpy as np
import main

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Spike Search"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        

        self.setWindowIcon(QtGui.QIcon('logo2.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)
        
        self.button = QPushButton(self)
        self.button.setText("Search")
        self.button.clicked.connect(self.onPressed)

        self.label = QLabel(self)
        #self.label.move(30,30)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.button)
        
        vbox.addLayout(hbox)
        
        self.setLayout(hbox)
        self.setLayout(vbox)
        
        vbox.addWidget(self.label)

        self.show()

    def onPressed(self):
        print(self.lineedit.text())
        rez = main.main(self.lineedit.text()) ##### added!
        self.label.setText(rez)
        



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())