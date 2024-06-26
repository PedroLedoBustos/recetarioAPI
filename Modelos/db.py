# Configuración y métodos para la base de datos
import mysql.connector
from mysql.connector import Error
from Modelos import Config

def crearConexion():
    connection=None

    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        print('Conexión exitosa a la base de datos MySQL')
    except Error as e:
        print(f'Error al conectarse a la base de datos MySQL: {e}')
    
    return connection

def cerrarConexion(conexion):
    if(conexion.is_connected()):
        conexion.close()
        print('Conexión cerrada a la base de datos')

