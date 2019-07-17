from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Tabung(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()

   def setupUi(self):
      self.resize(300, 100)
      self.move(320, 280)
      self.setWindowTitle('Volume Tabung')

      self.HitungButton = QPushButton('Hitung')
      self.cancelButton = QPushButton('Batal')

      hbox = QHBoxLayout()
      hbox.addWidget(self.HitungButton)
      hbox.addWidget(self.cancelButton)

      self.label1 = QLabel("Luas Alas ")
      self.nameLineEdit = QLineEdit()
      self.label2 = QLabel("Tinggi ")
      self.nameLineEdit2 = QLineEdit()
      self.label3 = QLabel("<b>Volume </b>")
      self.nameLineEdit3 = QLineEdit()

      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.nameLineEdit, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.nameLineEdit2, 1, 1)
      layout.addWidget(self.label3, 2, 0)
      layout.addWidget(self.nameLineEdit3, 2, 1)
      layout.addLayout(hbox, 3, 1)
      self.setLayout(layout)

      self.cancelButton.clicked.connect(self.cancelButtonClick)
      self.HitungButton.clicked.connect(self.HitungButtonClick)

   def cancelButtonClick(self):
      self.close()

   def HitungButtonClick(self):
      luas   = float(self.nameLineEdit.text())
      tinggi = float(self.nameLineEdit2.text())
      res    = luas * tinggi
      self.nameLineEdit3.setText(str(res))
