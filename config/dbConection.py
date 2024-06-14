# Configuración de la DB
import mysql.connector
import constants



# Crear conexión contra la base de datos
def conexionDB():
    '''Realiza una conexión contra la DB'''
    try:
        config_mysql = {'user': constants.USER_DB_SERVER,
        'password': constants.PASSWORD_DB_SERVER,
        'host': constants.IP_DB_SERVER,
        'database': constants.DB_SCHEMA,}

        conexion_mysql = mysql.connector.connect(**config_mysql)

        print("Conexión realizada correctamente.")        

    except mysql.connector.Error as MySQLError:        
        print(MySQLError)

conexionDB()