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
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowFlags(Qt.FramelessWindowHint)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        
        self.button1 = QPushButton('1', self)
        self.button2 = QPushButton('2', self)
        self.button3 = QPushButton('3', self)
        self.button4 = QPushButton('4', self)
        self.button5 = QPushButton('5', self)
        self.button6 = QPushButton('6', self)
        self.button7 = QPushButton('7', self)
        self.button8 = QPushButton('8', self)
        self.button9 = QPushButton('9', self)
        self.button0 = QPushButton('0', self)

        self.buttonDot = QPushButton('.', self)
        self.buttonSign = QPushButton('±', self)

        self.buttonPlus = QPushButton('+', self)
        self.buttonMinus = QPushButton('-', self)
        self.buttonTimes = QPushButton('×', self)
        self.buttonDivide = QPushButton('÷', self)
        self.buttonSqrt = QPushButton('√', self)

        self.buttonEquals = QPushButton('=', self)
        self.buttonC = QPushButton('AC', self)

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
            if(self.opOrg == '' or self.currOp == ''): return

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



        self.button1.clicked.connect(partial(addInput, 1))
        self.button2.clicked.connect(partial(addInput, 2))
        self.button3.clicked.connect(partial(addInput, 3))

        self.button4.clicked.connect(partial(addInput, 4))
        self.button5.clicked.connect(partial(addInput, 5))
        self.button6.clicked.connect(partial(addInput, 6))

        self.button7.clicked.connect(partial(addInput, 7))
        self.button8.clicked.connect(partial(addInput, 8))
        self.button9.clicked.connect(partial(addInput, 9))

        self.button0.clicked.connect(partial(addInput, 0))

        self.buttonC.clicked.connect(partial(simpleFn, ops.CLEAR))
        self.buttonSqrt.clicked.connect(partial(simpleFn, ops.SQRT))
        self.buttonSign.clicked.connect(partial(simpleFn, ops.SIGN))
        self.buttonDot.clicked.connect(partial(simpleFn, ops.DOT))


        self.buttonTimes.clicked.connect(partial(setOperation, ops.TIMES))
        self.buttonDivide.clicked.connect(partial(setOperation, ops.DIVISION))
        self.buttonPlus.clicked.connect(partial(setOperation, ops.ADDITION))
        self.buttonMinus.clicked.connect(partial(setOperation, ops.MINUS))
        self.buttonEquals.clicked.connect(equals)

        def toggleMaximize():
            if(self.isMaximized()):
                self.showNormal()
            else:
                self.showMaximized()

        topButtonStyle = "QPushButton { border-radius: 8px; "
        self.buttonClose = QPushButton('', self)
        self.buttonMinimize = QPushButton('', self)
        self.buttonMaximize = QPushButton('', self)
        self.buttonClose.clicked.connect(exit)
        self.buttonMinimize.clicked.connect(self.showMinimized)
        self.buttonMaximize.clicked.connect(toggleMaximize)


        self.buttonClose.setFixedSize(16, 16)
        self.buttonMinimize.setFixedSize(16, 16)
        self.buttonMaximize.setFixedSize(16, 16)
        self.buttonClose.setStyleSheet(topButtonStyle + "background-color: #ff5a52 }" + "QPushButton:hover { background-color: #9b3631 }")
        self.buttonMinimize.setStyleSheet(topButtonStyle + "background-color: #e6c029 }" + "QPushButton:hover { background-color: #8d7619 }")
        self.buttonMaximize.setStyleSheet(topButtonStyle + "background-color: #52c22b }" + "QPushButton:hover { background-color: #3a881f }")

        layoutTopBar = QHBoxLayout()
        layoutTopBar.addWidget(self.buttonClose)
        layoutTopBar.addWidget(self.buttonMinimize)
        layoutTopBar.addWidget(self.buttonMaximize)
        verticalSpacer = QSpacerItem(200, 35, QSizePolicy.Expanding, QSizePolicy.Fixed)
        layoutTopBar.addItem(verticalSpacer)
        layoutTopBar.setContentsMargins(10, 0, 0, 0)
        layoutTopBar.setSpacing(7)




        textStatus = QLabel()
        textStatus.setText("0")
        textStatus.setFont(QFont("Helvetica", 20))
        textStatus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        layoutText = QVBoxLayout()
        layoutText.addWidget(textStatus)

        layoutNumPad = QGridLayout()

        layoutNumPad.addWidget(self.buttonC, 0, 0)
        layoutNumPad.addWidget(self.buttonSign, 0, 1)
        layoutNumPad.addWidget(self.buttonSqrt, 0, 2)
        layoutNumPad.addWidget(self.buttonDivide, 0, 3)

        layoutNumPad.addWidget(self.button7, 1, 0)
        layoutNumPad.addWidget(self.button8, 1, 1)
        layoutNumPad.addWidget(self.button9, 1, 2)
        layoutNumPad.addWidget(self.buttonTimes, 1, 3)

        layoutNumPad.addWidget(self.button4, 2, 0)
        layoutNumPad.addWidget(self.button5, 2, 1)
        layoutNumPad.addWidget(self.button6, 2, 2)
        layoutNumPad.addWidget(self.buttonMinus, 2, 3)

        layoutNumPad.addWidget(self.button1, 3, 0)
        layoutNumPad.addWidget(self.button2, 3, 1)
        layoutNumPad.addWidget(self.button3, 3, 2)
        layoutNumPad.addWidget(self.buttonPlus, 3, 3)

        layoutNumPad.addWidget(self.button0, 4, 0, 1, 2)
        layoutNumPad.addWidget(self.buttonDot, 4, 2)
        layoutNumPad.addWidget(self.buttonEquals, 4, 3)

        layoutNumPad.setSpacing(0)

        textStatus.setStyleSheet("font-family: 'Helvetica Light'; font-size:60px; font-weight: 100; padding-right: 10px;")
        self.buttonStyle = "QPushButton { height: 45%; font-family: 'Helvetica Light'; font-size:30px; font-weight: 300; padding-left: 12px; padding-right: 12px; padding-top: 7px; padding-bottom: 7px; border: 1px solid #2b2d2f;"
        darkGrey = "background-color: #3f4143; } QPushButton:hover { background-color: #5b5e61 } QPushButton:pressed { background-color: #3f4143 }"
        grey = "background-color: #5f6062; } QPushButton:hover { background-color: #78797d } QPushButton:pressed { background-color: #5f6062 }"
        orange = "background-color: #ef7a1e; } QPushButton:hover { background-color: #ffac6a } QPushButton:pressed { background-color: #ef7a1e }"

        self.buttonMinus.setStyleSheet(self.buttonStyle + orange)
        self.buttonPlus.setStyleSheet(self.buttonStyle + orange)
        self.buttonDivide.setStyleSheet(self.buttonStyle + orange)
        self.buttonTimes.setStyleSheet(self.buttonStyle + orange)
        self.buttonEquals.setStyleSheet(self.buttonStyle + orange)




        self.button1.setStyleSheet(self.buttonStyle + grey)
        self.button2.setStyleSheet(self.buttonStyle + grey)
        self.button3.setStyleSheet(self.buttonStyle + grey)
        self.button4.setStyleSheet(self.buttonStyle + grey)
        self.button5.setStyleSheet(self.buttonStyle + grey)
        self.button6.setStyleSheet(self.buttonStyle + grey)
        self.button7.setStyleSheet(self.buttonStyle + grey)
        self.button8.setStyleSheet(self.buttonStyle + grey)
        self.button9.setStyleSheet(self.buttonStyle + grey)
        self.button0.setStyleSheet(self.buttonStyle + grey + "text-align: left; padding-left: 28px;")
        self.buttonC.setStyleSheet(self.buttonStyle + darkGrey)
        self.buttonSign.setStyleSheet(self.buttonStyle + darkGrey)
        self.buttonSqrt.setStyleSheet(self.buttonStyle + darkGrey)
        self.buttonDot.setStyleSheet(self.buttonStyle + grey)

        layout = QVBoxLayout()

        layoutNumPad.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layoutNumPad.setSpacing(0)

        layout.addLayout(layoutTopBar)
        layout.addLayout(layoutText)
        layout.addLayout(layoutNumPad)


        self.setStyleSheet("background-color: #2b2d2f; color: #fff")

        self.setLayout(layout)
        self.show()
        
    
    def keyPressEvent(self, e):
        match(e.key()):
            case Qt.Key_1:
                self.button1.click()
            case Qt.Key_2:
                self.button2.click()
            case Qt.Key_3:
                self.button3.click()
            case Qt.Key_4:
                self.button4.click()
            case Qt.Key_5:
                self.button5.click()
            case Qt.Key_6:
                self.button6.click()
            case Qt.Key_7:
                self.button7.click()
            case Qt.Key_8:
                self.button8.click()
            case Qt.Key_9:
                self.button9.click()
            case Qt.Key_0:
                self.button0.click()
            case Qt.Key_Period:
                self.buttonDot.click()
            case Qt.Key_C:
                self.buttonC.click()

app = QApplication(sys.argv)
ex = App()
app.exec()