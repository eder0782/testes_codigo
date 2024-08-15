from iqoptionapi.stable_api import IQ_Option
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LOGIN IQ OPTION')
        self.setGeometry(100, 100, 400, 300)

        # Layout
        layout = QVBoxLayout()

        # Widgets
        self.label1 = QLabel('LOGIN')
        self.input1 = QLineEdit()
        
        self.label2 = QLabel('SENHA')
        self.input2 = QLineEdit()
        
        self.result_label = QLabel('Resultado')
        self.result_display = QLabel('0')
        self.result_display.setAlignment(Qt.AlignCenter)
        
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        
        self.exit_button = QPushButton('Sair')
        self.exit_button.clicked.connect(self.close)

        # Add widgets to layout
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)
        layout.addWidget(self.login_button)
        layout.addWidget(self.exit_button)

        # Set the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def login(self):
        login_value = self.input1.text().strip()
        senha_value = self.input2.text().strip()

        # Validação dos campos de texto
        if not login_value or not senha_value:
            QMessageBox.warning(self, "Erro", "Ambos os campos devem estar preenchidos.")
            return
        try:
            API = IQ_Option(str(login_value), str(senha_value))
            API.connect()
            API.change_balance('PRACTICE')
            
            if API.check_connect() == True:
                self.result_display.setText('Conectado com Sucesso!')
            else:
                self.result_display.setText('Falha na conexão!')
        except Exception as e:
            QMessageBox.critical(self, "Erro de Conexão", f"Ocorreu um erro ao tentar conectar:\n{str(e)}")


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
