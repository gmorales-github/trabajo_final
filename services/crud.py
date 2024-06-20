# CRUD
from config.constants import *
from config.dbConfig import conexionDB



def testDB():
    '''Realiza una conexión de prueba contra la DB y se ejecuta un query de test.'''
    print("Realizando una prueba contra la DB...")
    
    # Realizó la conexión con la DB según los datos de configuración
    conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

    # creo el cursor
    cursor = conexion_mysql.cursor()

    # Generó un query sencillo de prueba
    test_query = TEST_QUERY
    
    # Ejecuto el query indicado
    cursor.execute(test_query)
    
    # Guardo los resultados y los muestro por la consola
    result = cursor.fetchall()
    if result:
        print(result) 
    else:
        print("No hay productos cargados.")
    
    # Cierro las conexiones
    conexion_mysql.close()
    cursor.close()

    print("Fin de la prueba contra la DB...")



def autenticar(user, password):
    '''Realiza el proceso de autenticación en la plataforma.
    Debe ingresar los parametros user y password'''
    # Realizó la conexión con la DB según los datos de configuración
    conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

    # creo el cursor
    cursor = conexion_mysql.cursor()

    # Generó un query para validar el ingreso a la plataforma
    auth_query = AUTH_QUERY + " " + "\"" + user + "\"" 
    
    # Ejecuto el query indicado
    cursor.execute(auth_query)
    
    # Guardo los resultados del query
    user_data = cursor.fetchall()

    # Vaĺido si el usuario existe en caso de no existir no se continua con las validaciones
    if user_data:
        # Extraigo el valor de la contraseñia y el valor del campo admin
        for data in user_data:            
            contrasenia, admin_valor = data

        # Valido si la contraseñia es correcta
        if contrasenia == password:
            print("Usted pudo ingresar a la plataforma")
            
            # Cierro las conexiones
            conexion_mysql.close()
            cursor.close()
            
            return True
        
        else:
            print("Usuario o contraseñia invalida.")

            # Cierro las conexiones
            conexion_mysql.close()
            cursor.close()
            
            return False        

    else:
        print("Usuario o contraseñia invalida.")

        # Cierro las conexiones
        conexion_mysql.close()
        cursor.close()
        
        return False
    
    
    



def listar_productos(cursor):
    query = "SELECT * FROM clientes"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return "No hay productos cargados."