from PySide6.QtWidgets import QListWidget,QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt


class Menu_configuracoes(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent) 
        self.ui_menu()
    
    
    
    def ui_menu(self):
        self.setGeometry(100,100, 600, 350)
        container_layout = QWidget()
        container_layout.setMinimumHeight(200)
        container_layout.setMinimumWidth(1000)
        
        layout_principal = QVBoxLayout()

        layout_input = QHBoxLayout()
        label_extencao = QLabel("Extenção :")
        layout_input.addWidget(label_extencao)
        input_extencao = QLineEdit()
        layout_input.addWidget(input_extencao)
        label_nome_pasta = QLabel("Nome da Pasta :")
        layout_input.addWidget(label_nome_pasta)
        input_nome_pasta = QLineEdit()
        layout_input.addWidget(input_nome_pasta)
        layout_principal.addLayout(layout_input)


        self.lista_extencoes = QListWidget()
        layout_principal.addWidget(self.lista_extencoes)

        container_layout.setLayout(layout_principal)
        
        self.setWindowModality(Qt.ApplicationModal)
        self.setLayout(layout_principal)
        
        
