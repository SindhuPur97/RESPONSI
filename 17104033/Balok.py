from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Balok(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()

   def setupUi(self):
      self.resize(300, 100)
      self.move(320, 280)
      self.setWindowTitle('Volume Balok')

      self.HitungButton = QPushButton('Hitung')
      self.cancelButton = QPushButton('Clear')

      hbox = QHBoxLayout()
      hbox.addWidget(self.HitungButton)
      hbox.addWidget(self.cancelButton)

      self.label1 = QLabel("Panjang ")
      self.nameLineEdit = QLineEdit()
      self.label2 = QLabel("Lebar ")
      self.nameLineEdit2 = QLineEdit()
      self.label3 = QLabel("Tinggi ")
      self.nameLineEdit3 = QLineEdit()
      self.label4 = QLabel("<b>Volume </b>")
      self.nameLineEdit4 = QLineEdit()

      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.nameLineEdit, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.nameLineEdit2, 1, 1)
      layout.addWidget(self.label3, 2, 0)
      layout.addWidget(self.nameLineEdit3, 2, 1)
      layout.addWidget(self.label4, 3, 0)
      layout.addWidget(self.nameLineEdit4, 3, 1)
      layout.addLayout(hbox, 4, 1)
      self.setLayout(layout)

      self.cancelButton.clicked.connect(self.cancelButtonClick)
      self.HitungButton.clicked.connect(self.HitungButtonClick)

   def cancelButtonClick(self):
      self.nameLineEdit.clear()
      self.nameLineEdit2.clear()
      self.nameLineEdit3.clear()
      self.nameLineEdit4.clear()

   def HitungButtonClick(self):
      panjang   = float(self.nameLineEdit.text())
      lebar     = float(self.nameLineEdit2.text())
      tinggi    = float(self.nameLineEdit3.text())
      res    = panjang * lebar * tinggi
      self.nameLineEdit4.setText(str(res))
