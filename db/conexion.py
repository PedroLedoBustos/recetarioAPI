import mysql.connector
from mysql.connector import Error
from config.configuracion import Configuracion

def crear_conexion():
    """Crea una conexión a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host=Configuracion.MYSQL_HOST,
            user=Configuracion.MYSQL_USER,
            password=Configuracion.MYSQL_PASSWORD,
            database=Configuracion.MYSQL_DB
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    """Cierra la conexión a la base de datos MySQL."""
    if conexion.is_connected():
        conexion.close()