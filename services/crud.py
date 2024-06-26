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
    
    

def listar_productos():
    '''Método para obtener todos los registros de la tabla productos.'''
    # Realizó la conexión con la DB según los datos de configuración
    conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

    # creo el cursor
    cursor = conexion_mysql.cursor()

    # Generó un query para validar el ingreso a la plataforma
    auth_query =  PRODUCTOS_QUERY 
    
    # Ejecuto el query indicado
    cursor.execute(auth_query)
    
    # Guardo los resultados del query
    productos_data = cursor.fetchall()

    # Cierro las conexiones
    conexion_mysql.close()
    cursor.close()

    return productos_data



def delete_producto(id_producto):
    '''Método para eliminar un producto mediante su id'''
    try:
        # Realizo la conexión con la DB según los datos de configuración
        conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

        # Creo el cursor
        cursor = conexion_mysql.cursor()

        # Genero un query para eliminar el producto usando consultas parametrizadas
        delete_producto_query = DELETE_PRODUCTO_QUERY + " %s"
        
        # Ejecuto el query indicado
        cursor.execute(delete_producto_query, (id_producto,))

        # Hago commit de la transacción
        conexion_mysql.commit()

    except Exception as e:
        print("Ocurrió un error:", e)
    
    finally:
        # Cierro el cursor y la conexión
        cursor.close()
        conexion_mysql.close()


def save_product(nombre_producto, precio, descripcion, stock):
    '''Método para eliminar un producto mediante su id'''
    try:
        # Realizo la conexión con la DB según los datos de configuración
        conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

        # Creo el cursor
        cursor = conexion_mysql.cursor()

        # Genero un query para guardar el producto nuevo usando consultas parametrizadas
        #save_product_query = SAVE_PRODUCTO_QUERY + " %s"
        save_product_query = SAVE_PRODUCTO_QUERY 
        
        # Ejecuto el query indicado
        cursor.execute(save_product_query, (nombre_producto,precio, descripcion, stock))

        # Hago commit de la transacción
        conexion_mysql.commit()

    except Exception as e:
        print("Ocurrió un error:", e)
    
    finally:
        # Cierro el cursor y la conexión
        cursor.close()
        conexion_mysql.close()


def update_product(id_producto, nombre_producto, precio, descripcion, stock):
    '''Método para actualizar un producto mediante su id'''
    try:
        # Realizo la conexión con la DB según los datos de configuración
        conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

        # Creo el cursor
        cursor = conexion_mysql.cursor()

        # Genero un query para guardar el producto nuevo usando consultas parametrizadas
        update_product_query = """
            UPDATE productos 
            SET nombre_producto = %s, precio = %s, descripcion = %s, stock = %s 
            WHERE id_producto = %s
        """

        # Ejecuto el query indicado
        cursor.execute(update_product_query, (nombre_producto,precio, descripcion, stock, id_producto))

        # Hago commit de la transacción
        conexion_mysql.commit()

    except Exception as e:
        print("Ocurrió un error:", e)
    
    finally:
        # Cierro el cursor y la conexión
        cursor.close()
        conexion_mysql.close()


def listar_ventas():
    '''Método para obtener todos los registros de la tabla ventas.'''
    # Realizó la conexión con la DB según los datos de configuración
    conexion_mysql = conexionDB(USER_DB_SERVER, PASSWORD_DB_SERVER, IP_DB_SERVER, DB_SCHEMA)

    # creo el cursor
    cursor = conexion_mysql.cursor()

    # Generó un query para validar el ingreso a la plataforma
    sales_query =  SALES_QUERY 
    
    # Ejecuto el query indicado
    cursor.execute(sales_query)
    
    # Guardo los resultados del query
    sales_data = cursor.fetchall()

    # Cierro las conexiones
    conexion_mysql.close()
    cursor.close()

    return sales_data