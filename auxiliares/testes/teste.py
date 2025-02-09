from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PySide6.QtGui import QIcon

class Organizador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selecionar Pasta")

        # Layout principal
        layout_principal = QVBoxLayout()
        
        # Criando o campo de entrada com botão 🔹
        layout_principal.addLayout(self.input_com_botao())

        self.setLayout(layout_principal)

    def input_com_botao(self):
        """Cria um QLineEdit com um botão de pasta embutido"""
        layout_input = QHBoxLayout()

        # Campo de entrada
        self.input_rota = QLineEdit()
        self.input_rota.setPlaceholderText("Selecione um diretório...")
        self.input_rota.setStyleSheet("padding: 5px; font-size: 14px;")

        # Botão de pasta
        botao_localizar = QPushButton()
        botao_localizar.setIcon(QIcon("/home/Projetos/Meus projetos pessoais/Organizador-de-pasta/icones/pasta_ carton_vazia.png"))  # Ícone da pasta
        botao_localizar.setFixedSize(32, 32)  # Tamanho do botão
        botao_localizar.setStyleSheet("border: none;")  # Remove borda do botão
        botao_localizar.clicked.connect(self.localizar)

        # Adiciona os elementos ao layout
        layout_input.addWidget(self.input_rota)
        layout_input.addWidget(botao_localizar)

        return layout_input

    def localizar(self):
        """Abre o QFileDialog e define o caminho no input"""
        diretorio = QFileDialog.getExistingDirectory(self, "Escolha um diretório")
        if diretorio:
            self.input_rota.setText(diretorio)

# Executando o programa
app = QApplication([])
janela = Organizador()
janela.show()
app.exec()
