# constantes
### DB CONFIGURATION ###
IP_DB_SERVER = "localhost"
PORT_DB_SERVER = 3306
USER_DB_SERVER = "root"
PASSWORD_DB_SERVER = "123456"
DB_SCHEMA = "dbtienda"


### QUERIES CONFIGURATION ###
TEST_QUERY = "SELECT * FROM Usuarios"
AUTH_QUERY = "SELECT contrasenia, admin FROM usuarios WHERE nombre_usuario = "
PRODUCTOS_QUERY = "SELECT * FROM productos"
SALES_QUERY = "SELECT * FROM ventas"
DELETE_PRODUCTO_QUERY = "DELETE FROM productos WHERE id_producto = "