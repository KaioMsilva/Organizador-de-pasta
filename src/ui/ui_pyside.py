from PySide6.QtWidgets import QFileDialog, QTextBrowser, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from acoes.organizador import organiza_pasta
from os import path

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
        self.setWindowTitle("Organizador de Pasta")
        self.setGeometry(100,100, 706, 404)
        
        # Adicionando Widget ou o layout no layout principal
        self.layout_principal.addWidget(self.layout_formulario_usuario())
        self.layout_principal.addLayout(self.exibir_dados())
        
        # Definindo layout principal
        self.setLayout(self.layout_principal)
        
    def layout_formulario_usuario(self):
        # Criando formulario
    
        # Instanciando QWidget, com ele é possivel colocar largura
        formulario_container = QWidget()
        formulario_container.setMaximumWidth(200)
        formulario_container.setMinimumHeight(404)
        formulario_container.setObjectName("Formulario_container")
        # Definindo formulario como layout do Widget, para pegar a largura definida a cima 
        layout_formulario = self.formulario()
        formulario_container.setLayout(layout_formulario)
        return formulario_container
    
    def formulario(self):
        form = QVBoxLayout()
        
        # Adicionando outos componentes do formulario
        form.addLayout(self.area_usuario())
        form.addLayout(self.informacoes_app())
        # form.addLayout(self.botoes())
        return form
    
    
    def area_usuario(self):
        # container_layout_input = QWidget()
        # container_layout_input.setMaximumHeight(100)
        
        layout_formulario = QVBoxLayout()
        
        # Texto
        label_input = QLabel("Caminho Pasta")
        label_input.setObjectName('Label_do_input')
        layout_formulario.addWidget(label_input, alignment=Qt.AlignHCenter)
        
        # Input do usuario
        layout_input = self.input_usuario()
        layout_formulario.addWidget(layout_input)
        
        
        # Titulo botão Organizar pasta
        botao_organizar = QPushButton("Organizar")
        botao_organizar.setObjectName("Botao_organizar")
        botao_organizar.setFixedSize(100,35)
        # Ação botão organizar 
        botao_organizar.clicked.connect(self.organizar_pasta)    
        
        layout_formulario.addWidget(botao_organizar, alignment=Qt.AlignHCenter)
        
        # return layout_input
        return layout_formulario
    
    def input_usuario(self):
        layout_container = QWidget()
        layout_container.setMinimumWidth(30)
        layout_container.setMaximumHeight(40)
        layout_container.setObjectName("Layout_input_usuario")

        # Layout Horizontal
        layout_input = QHBoxLayout()
        
        # Input
        self.input_rota = QLineEdit()
        self.input_rota.setObjectName("Input_rota")
        self.input_rota.setPlaceholderText("Informe o caminho")
        layout_input.addWidget(self.input_rota)
        
        # Titulo Botão localizar pasta
        botao_localizar = QPushButton("")
        botao_localizar.setObjectName("Botao_localizar")
        # Icone botão
        botao_localizar.setIcon(QIcon("src/assets/pasta_carton_vazia.png"))
        # Acão botão Localizar
        botao_localizar.clicked.connect(self.localizar)
        
        # adiciona Widget ao layout
        layout_input.addWidget(botao_localizar)


        layout_container.setLayout(layout_input)
        return layout_container
    
    def informacoes_app(self):
        layout_informacoes = QVBoxLayout()
        
        layout_informacoes.addStretch()
        versao = QLabel("V1.0")
        versao.setObjectName("Label_versao_sista")
        
        layout_informacoes.addWidget(versao, alignment=Qt.AlignHCenter)
        
        return layout_informacoes
    
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
        self.quadro_de_dados.setObjectName("Quadro_de_dados")
        
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
        if len(caminho) != 0 and path.isdir(caminho):
            organiza_pasta(caminho,self.quadro_de_dados)
           
        elif len(caminho) == 0:
            QMessageBox.warning(self,"Caminho invalido", "Caminho não pode ser vazio")
            
        else:
            QMessageBox.warning(self,"Caminho invalido", f"Caminho: '{caminho}' Não existe ")
            
        
            
            
            
            
            
# Tenho que testar caminho errado pra ver oq vai dar
