import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial
import math
from ops import *
from utils import specialCodes

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Kalkulator'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.size())
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        
        button1 = QPushButton('1', self)
        button2 = QPushButton('2', self)
        button3 = QPushButton('3', self)
        button4 = QPushButton('4', self)
        button5 = QPushButton('5', self)
        button6 = QPushButton('6', self)
        button7 = QPushButton('7', self)
        button8 = QPushButton('8', self)
        button9 = QPushButton('9', self)
        button0 = QPushButton('0', self)

        buttonDot = QPushButton('.', self)
        buttonSign = QPushButton('±', self)

        buttonPlus = QPushButton('+', self)
        buttonMinus = QPushButton('-', self)
        buttonTimes = QPushButton('×', self)
        buttonDivide = QPushButton('÷', self)
        buttonSqrt = QPushButton('√', self)

        buttonEquals = QPushButton('=', self)
        buttonC = QPushButton('C', self)

        self.opOrg = self.currOp = ''



        def setOperation(operation):
            if textStatus.text() in specialCodes:
                self.opOrg = "0"
                textStatus.setText("0")
            text = textStatus.text()
            self.opOrg = float(text)
            self.currOp = operation

        def addInput(i):
            text = textStatus.text()
            if(text in specialCodes or (self.currOp != '' and float(text) == self.opOrg)): text = ""

            text1 = text + str(i)
            textStatus.setText(text1)

        def equals():
            curInput = textStatus.text()
            text = doOp(self.currOp, float(self.opOrg), float(curInput))
            if text not in specialCodes and text.is_integer():   text = int(text)
            textStatus.setText(str(text))
            self.currOp = self.opOrg = self.currOp = ''

        def simpleFn(operation):
            match(operation):
                case ops.SIGN:
                    text = float(textStatus.text())
                    if text.is_integer():   text = int(text)
                    textStatus.setText(str((-1)*text    ))
                case ops.DOT:
                    text = textStatus.text()
                    if "." not in text: textStatus.setText(text + ".")
                case ops.SQRT:
                    try:
                        sqrt = math.sqrt(float(textStatus.text()))
                    except(ValueError):
                        textStatus.setText(specialCodes[2])
                        showDialogBox()
                        return
                    text = round(sqrt, 5)
                    if text.is_integer():   text = int(text)
                    textStatus.setText(str(text))
                case ops.CLEAR:
                    textStatus.setText("0")
                    self.currOp = self.opOrg = ''



        button1.clicked.connect(partial(addInput, 1))
        button2.clicked.connect(partial(addInput, 2))
        button3.clicked.connect(partial(addInput, 3))

        button4.clicked.connect(partial(addInput, 4))
        button5.clicked.connect(partial(addInput, 5))
        button6.clicked.connect(partial(addInput, 6))

        button7.clicked.connect(partial(addInput, 7))
        button8.clicked.connect(partial(addInput, 8))
        button9.clicked.connect(partial(addInput, 9))

        button0.clicked.connect(partial(addInput, 0))

        buttonC.clicked.connect(partial(simpleFn, ops.CLEAR))
        buttonSqrt.clicked.connect(partial(simpleFn, ops.SQRT))
        buttonSign.clicked.connect(partial(simpleFn, ops.SIGN))
        buttonDot.clicked.connect(partial(simpleFn, ops.DOT))


        buttonTimes.clicked.connect(partial(setOperation, ops.TIMES))
        buttonDivide.clicked.connect(partial(setOperation, ops.DIVISION))
        buttonPlus.clicked.connect(partial(setOperation, ops.ADDITION))
        buttonMinus.clicked.connect(partial(setOperation, ops.MINUS))
        buttonEquals.clicked.connect(equals)


        textStatus = QLabel()
        textStatus.setText("0")
        textStatus.setFont(QFont("Arial", 20))
        textStatus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        layout2 = QVBoxLayout()
        layout2.addWidget(textStatus)


        layoutTopFn = QHBoxLayout()

        layoutTopFn.addWidget(buttonC)
        layoutTopFn.addWidget(buttonSign)
        layoutTopFn.addWidget(buttonSqrt)
        layoutTopFn.addWidget(buttonDivide)

        layoutNumPad = QGridLayout()
        layoutNumPad.addWidget(button7, 0, 0)
        layoutNumPad.addWidget(button8, 0, 1)
        layoutNumPad.addWidget(button9, 0, 2)
        layoutNumPad.addWidget(buttonTimes, 0, 3)

        layoutNumPad.addWidget(button4, 1, 0)
        layoutNumPad.addWidget(button5, 1, 1)
        layoutNumPad.addWidget(button6, 1, 2)
        layoutNumPad.addWidget(buttonMinus, 1, 3)

        layoutNumPad.addWidget(button1, 2, 0)
        layoutNumPad.addWidget(button2, 2, 1)
        layoutNumPad.addWidget(button3, 2, 2)
        layoutNumPad.addWidget(buttonPlus, 2, 3)

        layoutNumPad.addWidget(button0, 3, 0, 1, 2)
        layoutNumPad.addWidget(buttonDot, 3, 2)
        layoutNumPad.addWidget(buttonEquals, 3, 3)

        layoutNumPad.setSpacing(0)
        buttonMinus.setStyleSheet("font-size:40px;background-color:#ef7a1e; border: 1px solid #3d3d3d")
        buttonPlus.setStyleSheet("font-size:40px;background-color:#ef7a1e; border: 1px solid #3d3d3d")
        buttonDivide.setStyleSheet("font-size:40px;background-color:#ef7a1e; border: 1px solid #3d3d3d")
        buttonTimes.setStyleSheet("font-size:40px;background-color:#ef7a1e; border: 1px solid #3d3d3d")
        buttonEquals.setStyleSheet("font-size:40px;background-color:#ef7a1e; border: 1px solid #3d3d3d")
        buttonEquals.setFixedSize(50, 50)
        buttonDivide.setFixedSize(50, 50)

        button1.setFixedSize(50, 50)
        button2.setFixedSize(50, 50)
        button3.setFixedSize(50, 50)
        button4.setFixedSize(50, 50)
        button5.setFixedSize(50, 50)
        button6.setFixedSize(50, 50)
        button7.setFixedSize(50, 50)
        button8.setFixedSize(50, 50)
        button9.setFixedSize(50, 50)
        buttonDot.setFixedSize(50, 50)
        button0.setFixedSize(100, 50)

        button1.setStyleSheet("font-size:40px;background-color:#4f4f4f; border: 1px solid #3d3d3d")
        button2.setStyleSheet("font-size:40px;background-color:#4f4f4f; border: 1px solid #3d3d3d")
        button3.setStyleSheet("font-size:40px;background-color:#4f4f4f; border: 1px solid #3d3d3d")
        button4.setStyleSheet("font-size:40px;background-color:#4f4f4f; border: 1px solid #3d3d3d")
        button5.setStyleSheet("font-size:40px;background-color:#4f4f4f; border: 1px solid #3d3d3d")

        layout = QVBoxLayout()
        layout.addLayout(layout2)
        layout.addLayout(layoutTopFn)
        layout.addLayout(layoutNumPad)

        
        layoutTopFn.setContentsMargins(0, 0, 0, 0)
        layoutNumPad.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet("background-color: #4f4f4f; color: #fff")

        self.setLayout(layout)
        self.show()
        
app = QApplication(sys.argv)
ex = App()
app.exec()