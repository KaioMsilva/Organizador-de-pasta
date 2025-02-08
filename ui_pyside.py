from PySide6.QtWidgets import QFileDialog, QCheckBox, QTextBrowser,QComboBox ,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox, QInputDialog
from PySide6.QtGui import QIcon
from acoes.organizador import organiza_pasta

class Organizador(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_organizador()
    # Tela com todos dos componentes
    def ui_organizador(self):
        
        # atribuindo uma classe para estilizar
        self.setObjectName("layout_principal")
        
        # Layout horizontal
        self.layout_principal = QHBoxLayout()
        
        # titulo e tamanho 
        self.setWindowTitle(" ")
        self.setGeometry(100,100, 706, 404)
        
        # Criando formulario
        
        # Instanciando QWidget, com ele é possivel colocar largura
        self.formulario_container = QWidget()
        self.formulario_container.setMaximumWidth(200)
        
        # Definindo formulario como layout do Widget, para pegar a largura definida a cima 
        layout_formulario = self.formulario()
        self.formulario_container.setLayout(layout_formulario)
                
        # Adicionando Widget no layout principal
        self.layout_principal.addWidget(self.formulario_container)
        self.layout_principal.addLayout(self.exibir_dados())
        
        # Definindo layout principal
        self.setLayout(self.layout_principal)
        
    def formulario(self):
        form = QVBoxLayout()
        
        # Adicionando outos componentes do formulario
        form.addWidget(self.input_usuario())
        # form.addLayout(self.botoes())
        return form
    
    def input_usuario(self):
        container_layout_input = QWidget()
        container_layout_input.setMaximumHeight(100)
        
        # Layout vertical
        layout_input = QVBoxLayout()
        
        # Texto
        label_input = QLabel("Caminho Da Pasta")
        
        # Input
        self.input_rota = QLineEdit()
        
        # Titulo Botão localizar pasta
        botao_localizar = QPushButton("")
        # Icone botão
        botao_localizar.setIcon(QIcon("icones/pasta_ carton_vazia.png"))
        # Acão botão Localizar
        botao_localizar.clicked.connect(self.localizar)
        
        # Titulo bptão Organizar pasta
        botao_organizar = QPushButton("Organizar")
        # Ação botão organizar 
        botao_organizar.clicked.connect(self.organizar_pasta)
        
        # adiciona Widget ao layout
        layout_input.addWidget(label_input)
        layout_input.addWidget(self.input_rota)
        layout_input.addWidget(botao_localizar)
        layout_input.addWidget(botao_organizar)
        container_layout_input.setLayout(layout_input)
    
        
        # return layout_input
        return container_layout_input
    
    # def botoes(self):
    #     # Layout vertical
    #     layout_botoes = QVBoxLayout()
        
    #     # Titulo Botão localizar pasta
    #     botao_localizar = QPushButton("")
    #     # Icone botão
    #     botao_localizar.setIcon(QIcon("icones/pasta_ carton_vazia.png"))
    #     # Acão botão Localizar
    #     botao_localizar.clicked.connect(self.localizar)
        
    #     # Titulo bptão Organizar pasta
    #     botao_organizar = QPushButton("Organizar")
    #     # Ação botão organizar 
    #     botao_organizar.clicked.connect(self.organizar_pasta)
        
    #     # adiciona Widget ao layout
    #     layout_botoes.addWidget(botao_localizar)
    #     layout_botoes.addWidget(botao_organizar)
    #     return layout_botoes
    
    def exibir_dados(self):
        # Layout vertical
        layout_saida_dados = QVBoxLayout()
        
        # Tabela para exibir informação
        self.quadro_de_dados = QTextBrowser() 
        
        # adiciona Widget ao layout
        layout_saida_dados.addWidget(self.quadro_de_dados)
        return layout_saida_dados
    
    def localizar(self):
        # Janela para selecionar diretorio
        diretorio = QFileDialog.getExistingDirectory(self, "Escolha um diretorio")
        # Limpa campo
        self.input_rota.clear()
        # Insere diretorio escolhido
        self.input_rota.insert(diretorio)
        
    def organizar_pasta(self):
        # Get caminho 
        caminho = self.input_rota.text()
        
        # Verifica se caminho não é vazio
        if caminho:
            organiza_pasta(caminho,self.quadro_de_dados)
        else:
            QMessageBox.warning(self,"Caminho invalido", "Informe um caminho valido")
            
            
            
            
            
# Tenho que testar caminho errado pra ver oq vai dar