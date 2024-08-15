from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QDoubleValidator
import sys

def somar():
    valor1 = campo1.text()
    valor2 = campo2.text()
    if valor1 and valor2:
        resultado = float(valor1) + float(valor2)
        resultado_label.setText(f'Resultado: {resultado}')
    else:
        resultado_label.setText('Preencha ambos os campos')

def limpar():
    campo1.clear()
    campo2.clear()
    resultado_label.setText('')

def sair():
    sys.exit()

def Janela():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 400, 300)
    win.setWindowTitle('Programa de Soma')

    global campo1, campo2, resultado_label

    campo1 = QLineEdit(win)
    campo1.setValidator(QDoubleValidator())  # Aceita valores do tipo float
    campo1.setPlaceholderText('Digite um número')
    campo1.move(50, 50)
    
    campo2 = QLineEdit(win)
    campo2.setValidator(QDoubleValidator())  # Aceita valores do tipo float
    campo2.setPlaceholderText('Digite outro número')
    campo2.move(200, 50)

    somar_bt = QPushButton(win)
    somar_bt.setText('Somar')
    somar_bt.move(50, 100)
    somar_bt.clicked.connect(somar)

    limpar_bt = QPushButton(win)
    limpar_bt.setText('Limpar')
    limpar_bt.move(150, 100)
    limpar_bt.clicked.connect(limpar)

    sair_bt = QPushButton(win)
    sair_bt.setText('Sair')
    sair_bt.move(250, 100)
    sair_bt.clicked.connect(sair)

    resultado_label = QLabel(win)
    resultado_label.setText('')
    resultado_label.move(50, 150)
    resultado_label.resize(300, 50)  # Aumentar o tamanho do label para caber o resultado

    win.show()
    sys.exit(app.exec_())

Janela()
