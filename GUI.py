from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout,QLineEdit, QLabel,QPushButton,QFormLayout,QInputDialog,QListWidgetItem,QListWidget
import sys
import sys
from os import listdir
from os.path import isfile, join
import re
import numpy as np
import main

class Window(QWidget):
    mypath=""
    def __init__(self):
        super().__init__()
        self.showDialog()
    def initUI(self):
        # Add button                                                                                                     
        self.btn = QPushButton('Select folder to files', self)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.showDialog)

    # Add label                                                                                                      
        self.le = QLabel(self)
        self.le.move(30, 62)
        self.le.resize(400,22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Enter folder')
        self.show()


    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Ennter folder:')
        if ok:
            mypath = str(text) 
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Enter folder')
        self.show()


        self.title = "Spike Search"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.setWindowIcon(QtGui.QIcon('logo2.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(lambda: self.onPressed(mypath))
        
        self.button = QPushButton(self)
        self.button.setText("Search")
        self.button.clicked.connect(lambda: self.onPressed(mypath))

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
    def onPressed(self,mypath):
        print(self.lineedit.text())
        print(mypath)
        rez = main.main(self.lineedit.text(),mypath+'/') ##### added!
        #mypath+rez

        print(rez)
        self.label.setOpenExternalLinks(True)
        item =""
        for i in range(len(rez)):
            if rez == "No results":
                item = '<p> No results <p>'
            else:
                item = item + '<p><a href = {}>{}</p>'.format(mypath + rez[i],rez[i])

        self.label.setText(item)
  ###########################################



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())