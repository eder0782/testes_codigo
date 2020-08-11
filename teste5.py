from  PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clique():
    print('Cliclou.')

def Janela():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,200,200)
    win.setWindowTitle('Meu primeiro Programa')

    label = QtWidgets.QLabel(win)
    label.setText('MEU LABEL')
    label.move(50,50)

    bt = QtWidgets.QPushButton(win)
    bt.setText('Clique Aqui')
    bt.clicked.__func__(clique())

    win.show()
    sys.exit(app.exec_())

Janela()