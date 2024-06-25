import tkinter as tk
from gui.products_menu import products_menu
from gui.sales_menu import sales_menu

def get_id():
    pass

def main_menu():    
    # Crear la ventana principal del menu
    window = tk.Tk()
    window.title("Menu principal")
    window.geometry("600x300")
    window.resizable(width=False, height=False)
    window['bg'] = '#b0c6ff'

    # Botón para ingresar a la gestión de productos
    btn_leer = tk.Button(window, text="Gestión de productos", command=lambda: products_menu())
    btn_leer.grid(row=1, column=3, pady=10, padx=200)
    
    # Botón para ingresar a la gestión de ventas
    btn_leer = tk.Button(window, text="Gestión de ventas", command=lambda: sales_menu())
    btn_leer.grid(row=2, column=3, pady=0, padx=0)

    # Botón para ingresar a la sección ganancias
    btn_leer = tk.Button(window, text="Ganancias", command=lambda: profits_menu())
    btn_leer.grid(row=3, column=3, pady=10, padx=0)

    # Botón para salir de la app
    btn_exit = tk.Button(window, text="Salir", command=exit)
    btn_exit.grid(row=4, column=3, pady=10, padx=0)

    # Ejecutar la aplicación
    window.mainloop()