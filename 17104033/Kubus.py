from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Kubus(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()

   def setupUi(self):
      self.resize(300, 100)
      self.move(320, 280)
      self.setWindowTitle('Volume Kubus')

      self.HitungButton = QPushButton('Hitung')
      self.cancelButton = QPushButton('Batal')

      hbox = QHBoxLayout()
      hbox.addWidget(self.HitungButton)
      hbox.addWidget(self.cancelButton)

      self.label1 = QLabel("Panjang Sisi")
      self.nameLineEdit = QLineEdit()
      self.label2 = QLabel("<b>Volume </b>")
      self.nameLineEdit2 = QLineEdit()

      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.nameLineEdit, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.nameLineEdit2, 1, 1)
      layout.addLayout(hbox, 2, 1)
      self.setLayout(layout)

      self.HitungButton.clicked.connect(self.HitungButtonClick)
      self.cancelButton.clicked.connect(self.cancelButtonClick)


   def cancelButtonClick(self):
            self.close()
   def HitungButtonClick(self):
            sisi = float(self.nameLineEdit.text())
            res = sisi * sisi * sisi
            self.nameLineEdit2.setText(str(res))
