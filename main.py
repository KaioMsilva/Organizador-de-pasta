from organizador import organiza_pasta
from funcoes import mostrar_diretorio
from tkinter import *
import tkinter as tk


# mostra diretorio atual
mostrar_diretorio()

# Janela principal
window = Tk()
window.title("Organizador de pasta")
window.config(padx=10, pady=50)

# Labels
website_label = Label(text="Path arquivo:")
website_label.grid(row=2, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()
add_button = Button(text="Oraganizar", width=36, command=lambda: organiza_pasta(website_entry))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

    




