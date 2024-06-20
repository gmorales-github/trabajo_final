# --- Login ---
import hashlib


def login():

    # Capturo los valores ingresados por el usuario
    user = input("Ingrese el nombre de usuario:")
    password = input("Ingrese su contraseñia: ")
    
    # Convierto a minúsculas
    user = user.lower()
    password = password.lower()

    # Genero el hash con la password ne sha256
    hash_password = hashlib.new("SHA256")
    hash_password.update(password.encode())
    
    print(hash_password.hexdigest())

    print(user, password)


