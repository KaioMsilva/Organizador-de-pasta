from PySide6.QtWidgets import QFileDialog, QCheckBox, QTextBrowser,QComboBox ,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QInputDialog
from organizador import organiza_pasta

class Organizador(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_organizador()
        
    def ui_organizador(self):
        self.layout_principal = QHBoxLayout()
        self.setWindowTitle("Organizador de pastas")
        self.setGeometry(100,100, 300, 100)
        
        self.layout_principal.addLayout(self.formulario())
        self.layout_principal.addLayout(self.exibir_dados())
        
        
        self.setLayout(self.layout_principal)
        
    def formulario(self):
        form = QVBoxLayout()
        form.addLayout(self.input_usuario())
        form.addLayout(self.botoes())
        return form
    
    def input_usuario(self):
        layout_input = QVBoxLayout()
        label_input = QLabel("Informe o caminho")
        self.input_rota = QLineEdit()
        
        layout_input.addWidget(label_input)
        layout_input.addWidget(self.input_rota)
        
        return layout_input
    
    def exibir_dados(self):
        layout_saida_dados = QVBoxLayout()
        self.quadro_de_dados = QTextBrowser() 
        layout_saida_dados.addWidget(self.quadro_de_dados)
        return layout_saida_dados
    
    def botoes(self):
        layout_botoes = QVBoxLayout()
        botao_localizar = QPushButton("localizar")
        botao_localizar.clicked.connect(self.localizar)
        botao_organizar = QPushButton("Organizar")
        botao_organizar.clicked.connect(self.organizar_pasta)
        
        layout_botoes.addWidget(botao_localizar)
        layout_botoes.addWidget(botao_organizar)
        return layout_botoes
    
    def localizar(self):
        diretorio = QFileDialog.getExistingDirectory(self, "Escolha um diretorio")
        self.input_rota.clear()
        self.input_rota.insert(diretorio)
        
    def organizar_pasta(self):
        caminho = self.input_rota.text()
        if caminho:
            organiza_pasta(caminho,self.quadro_de_dados)
        else:
            QMessageBox.warning(self,"Caminho invalido", "Informe um caminho valido")