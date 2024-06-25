import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from services.crud import listar_productos
from services.crud import delete_producto


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

def get_id(tv):
    '''Tomo el id_producto del elemento seleccionado en la lista de la tabla.'''    
    seleccion = tv.selection()

    if seleccion:
        item = seleccion[0]
        item_values = tv.item(item, 'values')
        id = item_values[0]
        return id
    
    else:
        # Despliego el msg de alerta
        messagebox.showerror("Error", "Debe seleccionar un registro para poder borrarlo")        

    



def delete(tv):
    '''Método para eliminar el registro seleccionado.'''
    # Invoco al método para obtener el id
    id = get_id(tv=tv)

    if id:
        #Invoco al método para eliminar el producto por id_producto
        delete_producto(id_producto=id)

        # Invoco al método refresh para actualizar los datos de la tabla
        refresh_table(tv=tv)



def products_menu():
    # Obtengo la lista de todos los productos
    productos = listar_productos()
    
    # Crear la ventana principal del menu
    window = tk.Tk()
    window.title("Gestión de productos")
    window.geometry("1225x600")
    window.resizable(width=False, height=False)
    window['bg'] = '#b0c6ff'

    # Cargo las columnas 
    columns = ("id_producto", "nombre_producto", "precio", "descripcion", "stock", "id_marca")
    
    # Genero la tabla
    tv = ttk.Treeview(window, columns=columns, show="headings")
    tv.pack()

    # Recorro la lista de columnas para generar dinámicamente los encabezados
    for head in columns:
        tv.heading(head, text=head, anchor=tk.CENTER)

    # Recorro la lista de columnas para generar las columnas dinámicamente en la tabla
    for column in columns:
        tv.column(column, anchor='e')
    
    # Recorro la lista de productos para insertar los valores dinámicamente en la tabla
    for producto in productos:
        tv.insert('', tk.END, values=producto)
    
    tv.grid(row=0, column=2, padx=10, pady=10)
    
    # Botón para agregar un nuevo producto
    btn_leer = tk.Button(window, text="Nuevo", command=lambda: get_id(tv))
    btn_leer.grid(row=1, column=2, pady=10)
    
    # Botón para editar el registro seleccionado
    btn_leer = tk.Button(window, text="Editar", command=lambda: get_id(tv))
    btn_leer.grid(row=2, column=2, pady=10)
    
    # Botón para eliminar el registro seleccionado
    btn_leer = tk.Button(window, text="Eliminar", command=lambda: delete(tv))
    btn_leer.grid(row=3, column=2, pady=10)

    # Botón para refrescar los datos de la tabla
    btn_refrescar = tk.Button(window, text="Actualizar", command=lambda: refresh_table(tv))
    btn_refrescar.grid(row=4, column=2, pady=10)    

    # Botón para salir de la app
    btn_exit = tk.Button(window, text="Salir", command=exit)
    btn_exit.grid(row=5, column=2, pady=10)

    # Ejecutar la aplicación
    window.mainloop()