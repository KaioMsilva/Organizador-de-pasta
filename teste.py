from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSizePolicy
import sys

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SizePolicy Responsivo")
        self.setGeometry(100, 100, 400, 300)

        botao1 = QPushButton("Botão 1")
        botao2 = QPushButton("Botão 2")

        # Permite que os botões cresçam
        botao1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        botao2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(botao1)
        layout.addWidget(botao2)

        self.setLayout(layout)

app = QApplication(sys.argv)
janela = Janela()
janela.show()
sys.exit(app.exec())
