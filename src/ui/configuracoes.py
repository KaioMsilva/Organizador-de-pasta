from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
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
        
        layout = QVBoxLayout()
        container_layout.setLayout(layout)
        
        self.setWindowModality(Qt.ApplicationModal)
        self.setLayout(layout)
        
        
