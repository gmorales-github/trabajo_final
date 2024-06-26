import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from services.crud import listar_ventas


def refresh_table(tv):
    '''Método para actualizar el contenido de la tabla.'''
    # Obtengo la lista de todas las ventas actualizada
    ventas = listar_ventas()
    
    # Borro todos los elementos actuales del Treeview
    for item in tv.get_children():
        tv.delete(item)
    
    # Inserto los productos actualizados en el Treeview
    for venta in ventas:
        tv.insert('', tk.END, values=venta)

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

def sales_menu(window):
    # Elimino la ventana menu principal
    window.destroy()
    # Obtengo la lista de todos los productos
    ventas = listar_ventas()
    
    # Crear la ventana principal del menu
    window = tk.Tk()
    window.title("Gestión de ventas")
    window.geometry("1225x600")
    window.resizable(width=False, height=False)
    window['bg'] = '#b0c6ff'

    # Cargo las columnas 
    columns = ("id_venta", "id_usuario", "fecha", "total_final")
    
    # Genero la tabla
    tv = ttk.Treeview(window, columns=columns, show="headings")
    tv.pack()

    # Recorro la lista de columnas para generar dinámicamente los encabezados
    for head in columns:
        tv.heading(head, text=head, anchor=tk.CENTER)

    # Recorro la lista de columnas para generar las columnas dinámicamente en la tabla
    for column in columns:
        tv.column(column, anchor='e')
    
    # Recorro la lista de ventas para insertar los valores dinámicamente en la tabla
    for venta in ventas:
        tv.insert('', tk.END, values=venta)
    
    tv.grid(row=0, column=2, padx=10, pady=10)
    
    # Botón para agregar una nueva venta
    btn_leer = tk.Button(window, text="Nueva venta", command=lambda: get_id(tv))
    btn_leer.grid(row=1, column=2, pady=10)
    
    # Botón para refrescar los datos de la tabla
    btn_refrescar = tk.Button(window, text="Actualizar", command=lambda: refresh_table(tv))
    btn_refrescar.grid(row=2, column=2, pady=10)

    # Botón para volver al menu principal
    btn_refrescar = tk.Button(window, text="Menu principal", command=lambda: main_menu(tv))
    btn_refrescar.grid(row=3, column=2, pady=10)    

    # Botón para salir de la app
    btn_exit = tk.Button(window, text="Salir", command=exit)
    btn_exit.grid(row=4, column=2, pady=10)

    # Ejecutar la aplicación
    window.mainloop()