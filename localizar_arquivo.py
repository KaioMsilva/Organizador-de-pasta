from tkinter import filedialog, END

def localizar(entrada):
    path_arquivo = filedialog.askdirectory()
    entrada.delete(0,END)
    entrada.insert(0, path_arquivo)