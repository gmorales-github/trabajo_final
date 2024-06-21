import tkinter as tk
from tkinter import ttk
 
def main_menu():
    # Crear la ventana principal del menu
    window = tk.Tk()
    window.title("Menu principal")
    window.geometry("600x600")
    window.resizable(width=False, height=False)
    window['bg'] = '#fb0'


    # Cargo las columnas 
    columns = ("id_usuario", "nombre_usuario", "contrasenia")
    
    tv = ttk.Treeview(window, columns = columns, show="headings")
    tv.heading ('id_usuario', text='id usuario', anchor=tk.CENTER)
    tv.heading ('nombre_usuario', text="nombre usuario", anchor=tk.CENTER)
    tv.heading ('contrasenia', text="contraseña", anchor=tk.CENTER)

    tv.insert ('', tk.END, values = ('1', 'admin1', 'adminpass1'))
    tv.insert ('', tk.END, values = ('2', 'usuario1', 'adminpass1'))
    tv.insert ('', tk.END, values = ('3', 'usuario2', 'adminpass1'))
    tv.grid (row=0, column=2, padx=10, pady=50)

    # Ejecutar la aplicación
    window.mainloop()