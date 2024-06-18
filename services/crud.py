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



def listar_productos(cursor):
    query = "SELECT * FROM clientes"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return "No hay productos cargados."