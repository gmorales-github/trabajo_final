# Módulo de configuración de la conexión de la DB
import mysql.connector


# Crear conexión contra la base de datos
def conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA):
    '''Realiza una conexión contra la DB'''
    try:
        config_mysql = {'user': USER_DB_SERVER,
        'password': PASSWORD_DB_SERVER,
        'host': IP_DB_SERVER,
        'database': DB_SCHEMA,}

        conexion_mysql = mysql.connector.connect(**config_mysql)

        #print("Conexión realizada correctamente.")

        return conexion_mysql        

    except mysql.connector.Error as MySQLError:        
        print(MySQLError)