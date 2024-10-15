from organizador import organiza_pasta
from funcoes import mostrar_diretorio
from localizar_arquivo import localizar
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter as tk



# mostra diretorio atual
mostrar_diretorio()

# Janela principal
janela = Tk()
janela.title("Organizador de pasta")
janela.config(padx=20, pady=50)

# icone sistema
icone = tk.PhotoImage(file="icone.png")
janela.iconphoto(False,icone)

# Labels
janela_label = Label(master=janela,text="Path arquivo:")
janela_label.grid(row=2, column=0)

# Entries
janela_entry = Entry(master=janela,width=35)
janela_entry.grid(row=2, column=1, columnspan=2)
janela_entry.focus()

# saidas
janela_exit = ScrolledText(janela, height=5, width=50)
janela_exit.grid(row = 5, column=1, columnspan=3)
janela_exit.config(state=DISABLED)


# Botôes
add_button = Button(master=janela,text="Oraganizar", width=18, command=lambda: organiza_pasta(janela_entry, janela_exit))
add_button.grid(row=4, column=2, columnspan=1)

add_button = Button(master=janela,text="localizar", width=18, command=lambda: localizar(janela_entry))
add_button.grid(row=4, column=1, columnspan=1)





janela.mainloop()
