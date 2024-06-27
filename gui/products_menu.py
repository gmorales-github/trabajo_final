import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from services.crud import listar_productos, delete_producto
from gui.add_product_menu import new_product
from gui.update_product_menu import update_product
from services.crud import obtener_permiso


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

def get_data_product(tv):
    '''Obtengo los datos del elemento seleccionado en la lista de la tabla.'''    
    seleccion = tv.selection()

    if seleccion:
        item = seleccion[0]
        item_values = tv.item(item, 'values')
        return item_values
    
    else:
        # Despliego el msg de alerta
        messagebox.showerror("Error", "Debe seleccionar un registro para poder editarlo")
        
    
def update_product_menu(tv):
    # Cargo la variable data con el contenido del registro del producto de la lista
    data = get_data_product(tv)

    if data:
        # Invoco al menu editar producto
        update_product(tv, data)




def delete(tv):
    '''Método para eliminar el registro seleccionado.'''
    # Invoco al método para obtener el id
    id = get_id(tv=tv)

    if id:
        #Invoco al método para eliminar el producto por id_producto
        delete_producto(id_producto=id)

        # Invoco al método refresh para actualizar los datos de la tabla
        refresh_table(tv=tv)



def products_menu(window, user):
    '''Método que genera la ventana del menu producto'''
    # Elimino la ventana menu principal
    window.destroy()
    # Obtengo la lista de todos los productos
    productos = listar_productos()
    
    # Obtengo los permisos del usuario
    admin_value = obtener_permiso(user=user)

    
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

    # Según los permisos limito las acciones de los usuarios. admin = 1
    if admin_value[0] == 1:
        # Botón para agregar un nuevo producto
        btn_product = tk.Button(window, text="Nuevo", command=lambda: new_product(tv))
        btn_product.grid(row=1, column=2, pady=10)
    
        # Botón para editar el producto seleccionado
        btn_edit = tk.Button(window, text="Editar", command=lambda: update_product_menu(tv))
        btn_edit.grid(row=2, column=2, pady=10)
    
        # Botón para eliminar el registro seleccionado
        btn_delete = tk.Button(window, text="Eliminar", command=lambda: delete(tv))
        btn_delete.grid(row=3, column=2, pady=10)

    else:
        #config(state='disabled')
        # Botón para agregar un nuevo producto
        btn_product = tk.Button(window, text="Nuevo", command=lambda: new_product(tv))
        btn_product.grid(row=1, column=2, pady=10)
        btn_product.config(state='disabled')
    
        # Botón para editar el producto seleccionado
        btn_edit = tk.Button(window, text="Editar", command=lambda: update_product_menu(tv))
        btn_edit.grid(row=2, column=2, pady=10)
        btn_edit.config(state='disabled')
    
        # Botón para eliminar el registro seleccionado
        btn_delete = tk.Button(window, text="Eliminar", command=lambda: delete(tv))
        btn_delete.grid(row=3, column=2, pady=10)
        btn_delete.config(state='disabled')
    
    # Botón para refrescar los datos de la tabla
    btn_refrescar = tk.Button(window, text="Actualizar", command=lambda: refresh_table(tv))
    btn_refrescar.grid(row=4, column=2, pady=10)    

    # Botón para salir de la app
    btn_exit = tk.Button(window, text="Salir", command=exit)
    btn_exit.grid(row=5, column=2, pady=10)

    # Ejecutar la aplicación
    window.mainloop()