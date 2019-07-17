from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Kubus import *
from Balok import *
from Tabung import *

class MainForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()

   def setupUi(self):
      self.resize(400, 100)
      self.move(300, 300)
      self.setWindowTitle('Menghitung Volume Bangun Ruang')

      self.label1 = QLabel('<b><font size=5>Pilih Volume Bangun Ruang Yang Ingin Dicari</font></b>')

      icon1 = QIcon('icon/kubus-icon.png')
      self.kubusButton = QPushButton('\tKubus')
      self.kubusButton.setIcon(icon1)

      icon2 = QIcon('icon/balok-icon.png')
      self.balokButton = QPushButton('\tBalok')
      self.balokButton.setIcon(icon2)

      icon3 = QIcon('icon/tabung1-icon.png')
      self.tabungButton = QPushButton('\tTabung')
      self.tabungButton.setIcon(icon3)

      hbox = QHBoxLayout()
      hbox.addWidget(self.kubusButton)
      hbox.addWidget(self.balokButton)
      hbox.addWidget(self.tabungButton)

      layout = QVBoxLayout()
      layout.addWidget(self.label1)
      layout.addLayout(hbox)
      self.setLayout(layout)

      self.kubusButton.clicked.connect(self.kubusButtonClick)
      self.balokButton.clicked.connect(self.balokButtonClick)
      self.tabungButton.clicked.connect(self.tabungButtonClick)

   def kubusButtonClick(self):
       self.form = Kubus()
       self.form.show()

   def balokButtonClick(self):
      self.form = Balok()
      self.form.show()

   def tabungButtonClick(self):
      self.form = Tabung()
      self.form.show()
