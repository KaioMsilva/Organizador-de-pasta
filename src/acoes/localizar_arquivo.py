from tkinter import filedialog, END
from PySide6.QtWidgets import QFileDialog

# def localizar(entrada):
#     path_arquivo = filedialog.askdirectory()
#     entrada.delete(0,END)
#     entrada.insert(0, path_arquivo)


def localizar(entrada):
    path_arquivo = QFileDialog.askdirectory()
    entrada.delete(0,END)
    entrada.insert(0, path_arquivo)
    
