import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela com Fundo Personalizado")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Exemplo de fundo personalizado!"))
        self.setLayout(layout)

# Criando a aplicação
app = QApplication(sys.argv)

# 🔹 Aplicando a cor de fundo GLOBALMENTE a toda a janela
app.setStyleSheet("QWidget { background-color: #252B36; color: white; }")

# Criando e exibindo a janela
janela = MinhaJanela()
janela.show()
sys.exit(app.exec())
