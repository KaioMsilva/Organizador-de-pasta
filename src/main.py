# from ui import inicia_organizador

# if __name__ == '__main__':
#     inicia_organizador()

from PySide6.QtWidgets import QApplication
from ui.ui_pyside import Organizador

if __name__ == '__main__':
    app = QApplication([])
    
    with open("src/ui/style.qss", "r") as arquivo:
        app.setStyleSheet(arquivo.read())
    
    
    
    organizador = Organizador()
    organizador.show()
    app.exec()
