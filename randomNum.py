from PyQt6.QtWidgets import (QLineEdit, QWidget, QGridLayout, QPushButton, QLabel)
from PyQt6.QtCore import QTime, Qt
from random import randint


class Random(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGridLayout()

        self.resize(500, 400)
        self.move(int(1920/2 - 500/2), int(1080/2 - 400/2))

        self.setWindowTitle("随机抽号软件")
        self.show()

    def getNums(self):
        begin = int(self.fromEdit.text())
        end = int(self.toEdit.text())
        randomNumber = randint(begin, end)
        self.randomNumberWidget.setText(str(randomNumber))
        self.dateTime = QTime.currentTime()
        self.dateTimeWidget.setText("上一次抽号时间: %s" % self.dateTime.toString())

    def setGridLayout(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(9)

        self.to = QLabel(self)
        self.to.setText("至")
        self.to.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.to.setStyleSheet("""
font-size: 16px;""")

        self.randomNumberWidget = QLabel(self)
        self.randomNumberWidget.setText("-1")
        self.randomNumberWidget.setStyleSheet("""
font-size: 60px;""")
        self.randomNumberWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fromEdit = QLineEdit("1")
        self.toEdit = QLineEdit("53")

        self.dateTime = QTime.currentTime()
        self.dateTimeWidget = QLabel(self)
        self.dateTimeWidget.setText("上一次抽号时间: Nil")
        self.dateTimeWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.getRandomButton = QPushButton("开始抽号")
        self.getRandomButton.setStyleSheet("""
background-color: #262626;
color: #FFFFFF;
""")

        self.grid.addWidget(self.fromEdit, 1, 0)
        self.grid.addWidget(self.to, 1, 1)
        self.grid.addWidget(self.toEdit, 1, 2)
        self.grid.addWidget(self.randomNumberWidget, 2, 1)
        self.grid.addWidget(self.getRandomButton, 3, 1)
        self.grid.addWidget(self.dateTimeWidget, 3, 2)

        self.getRandomButton.clicked.connect(self.getNums)


        self.setLayout(self.grid)
