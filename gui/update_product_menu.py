import tkinter as tk
from services.crud import listar_productos
from services.crud import update_product as update


def refresh_table(tv):
    '''Método para actualizar el contenido de la tabla.'''
    # Obtengo la lista de todos los productos actualizada
    productos = listar_productos()
    
    # Borro todos los elementos actuales del Treeview
    for item in tv.get_children():
        tv.delete(item)
    
    # Inserto los productos actualizados en el Treeview
    for producto in productos:
        tv.insert('', tk.END, values=producto)



def check_number(char):
    # Validar que el carácter ingresado sea numérico o un punto decimal
    return char.isdigit() or char == '.'

def check_integer(char):
    # Validar que el carácter ingresado sea numérico
    return char.isdigit()

def update_product(tv, data):
    # Extraigo los valores de la lista data
    columnas_productos = ["id_producto", "nombre_producto", "precio", "descripcion" , "stock"]

    # Usar zip para combinar las listas y dict para convertirlas en un diccionario
    product = dict(zip(columnas_productos, data))

    # Crear la ventana principal
    window = tk.Tk()
    window.title("Menu editar producto")
    window.geometry("500x450")
    window.resizable(width=False, height=False)
    window['bg'] = '#b0c6ff'

    # Crear y colocar etiquetas y entradas de texto
    label_productid = tk.Label(window, text="ID producto:")
    label_productid.grid(row=0, column=0, padx=5, pady=10)

    entry_productid = tk.Entry(window)
    entry_productid.insert(0, product["id_producto"])    
    entry_productid.grid(row=0, column=1, padx=5, pady=10)
    entry_productid.config(state='disabled')

    label_productname = tk.Label(window, text="Nombre del producto:")
    label_productname.grid(row=1, column=0, padx=5, pady=50)

    entry_productname = tk.Entry(window)
    entry_productname.insert(0, product["nombre_producto"])
    entry_productname.grid(row=1, column=1, padx=5, pady=50)

    label_price = tk.Label(window, text="Precio")
    label_price.grid(row=2, column=0, padx=5, pady=5)

    # TODO: Corregir el error en la validación y casting de datos
    #entry_price_var = tk.StringVar()
    #validate_price_command = window.register(check_number)    
    #entry_price = tk.Entry(window, textvariable=entry_price_var, validate="key", validatecommand=(validate_price_command, '%S'))
    entry_price = tk.Entry(window)
    entry_price.insert(0, product["precio"])
    entry_price.grid(row=2, column=1, padx=5, pady=5)

    label_description = tk.Label(window, text="Descripción")
    label_description.grid(row=3, column=0, padx=5, pady=5)

    entry_description = tk.Entry(window)
    entry_description.insert(0, product["descripcion"])
    entry_description.grid(row=3, column=1, padx=5, pady=5)

    label_stock = tk.Label(window, text="Cantidad")
    label_stock.grid(row=4, column=0, padx=5, pady=5)

    entry_stock_var = tk.StringVar()
    validate_stock_command = window.register(check_integer)
    entry_stock = tk.Entry(window, textvariable=entry_stock_var, validate="key", validatecommand=(validate_stock_command, '%S'))
    entry_stock.insert(0, product["stock"])
    entry_stock.grid(row=4, column=1, padx=5, pady=5)

    # Crear y colocar el botón de actualizar
    button_update = tk.Button(window, text="Actualizar", command=lambda: (update(id_producto=product["id_producto"],nombre_producto=entry_productname.get(), precio=entry_price.get(), descripcion=entry_description.get(), stock=entry_stock.get()), refresh_table(tv)))    
    button_update.grid(row=10, column=0, columnspan=5, pady=50)

    # Crear y colocar el botón de cancelar
    button_exit = tk.Button(window, text="Cancelar", command=window.destroy)
    button_exit.grid(row=10, column=2, columnspan=5, pady=50)

    # Ejecutar la aplicación
    window.mainloop()