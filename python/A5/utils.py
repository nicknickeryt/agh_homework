from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
specialCodes = ["0", "Dziel/0!", "Nierzeczywista!"]

def showDialogBox():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Podano nieprawidłową wartość.")
    msg.setWindowTitle("Błąd!")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()