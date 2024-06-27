from services.crud import autenticar
from gui.main_menu import main_menu
import tkinter as tk
from tkinter import messagebox



def main():
    '''Main'''
    print("-- Iniciando programa ---")
    print("-- Finalizando programa ---")



# Función que se ejecuta al presionar el botón de login
def login():
    '''Función que permite enviar la credeenciales a la DB para su validación'''
    if autenticar(user=entry_username.get(), password=entry_password.get()):        
        # Elimino la ventana de login
        window.destroy()
        # Ingreso al menu principal
        main_menu()
                
        

    else:
        # Despliego el msg de alerta
        messagebox.showerror("Login", "Usuario o contraseña incorrectos") 
    
    

# Crear la ventana principal
window = tk.Tk()
window.title("Menu de inicio")
window.geometry("410x300")
window.resizable(width=False, height=False)
window['bg'] = '#b0c6ff'

# Crear y colocar etiquetas y entradas de texto
label_username = tk.Label(window, text="Usuario")
label_username.grid(row=0, column=0, padx=5, pady=50)

entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1, padx=5, pady=50)

label_password = tk.Label(window, text="Contraseña")
label_password.grid(row=1, column=0, padx=5, pady=5)

entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Crear y colocar el botón de login
button_login = tk.Button(window, text="Ingresar", command=login)
button_login.grid(row=2, column=0, columnspan=5, pady=50)

# Crear y colocar el botón de salir
button_exit = tk.Button(window, text="Salir", command=exit)
button_exit.grid(row=2, column=100, columnspan=5, pady=50)

# Ejecutar la aplicación
window.mainloop()



if __name__ == '__main__':
    main()