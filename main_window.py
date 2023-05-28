from typing import Optional
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QFrame, QVBoxLayout, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from verificar_numero import verificar_numero

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculo Cúbico')
        self.setFixedSize(QSize(300,250))
        self.setWindowIcon(QIcon('cube.png'))
        self.setStyleSheet('background-color: #D8BFD8; font-weight: bold;')

        self.label_largura = QLabel('LARGURA:')
        self.label_altura = QLabel('ALTURA:')
        self.label_comprimento = QLabel('COMPRIMENTO:')
        self.label_resultado = QLabel()

        self.line_edit_largura = QLineEdit()
        self.line_edit_altura = QLineEdit()
        self.line_edit_comprimento = QLineEdit()

        self.button = QPushButton('CALCULAR')
        self.button.clicked.connect(self.calcular)

        layout = QVBoxLayout()
        layout.addWidget(self.label_largura)
        layout.addWidget(self.line_edit_largura)
        layout.addWidget(self.label_altura)
        layout.addWidget(self.line_edit_altura)
        layout.addWidget(self.label_comprimento)
        layout.addWidget(self.line_edit_comprimento)
        layout.addWidget(self.label_resultado)
        layout.addWidget(self.button)

        container = QFrame()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calcular(self):
        aviso = verificar_numero(self.line_edit_largura.text(), self.line_edit_altura.text(), self.line_edit_comprimento.text())
        if aviso != None:
            self.label_resultado.setText(aviso)
        else:
            resultado =  str(float(self.line_edit_largura.text()) * float(self.line_edit_altura.text()) * float(self.line_edit_comprimento.text()))
            resultado = float(resultado)
            self.label_resultado.setText(f'O RESULTADO = {resultado}m²')
    
    
            

        



