from db.conexion import crear_conexion, cerrar_conexion
from modelos.receta import Receta

def agregar_receta(titulo, descripcion, ingredientes, pasos):
    """Agrega una nueva receta a la base de datos."""
    conexion = crear_conexion()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("INSERT INTO recetas (titulo, descripcion, ingredientes, pasos) VALUES (%s, %s, %s, %s)",
                       (titulo, descripcion, ingredientes, pasos))
        conexion.commit()
        receta_id = cursor.lastrowid
        cerrar_conexion(conexion)
        return receta_id
    except Exception as e:
        cerrar_conexion(conexion)
        raise e

def obtener_todas_recetas():
    """Obtiene todas las recetas de la base de datos."""
    conexion = crear_conexion()
    cursor = conexion.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM recetas")
        filas = cursor.fetchall()
        cerrar_conexion(conexion)
        
        recetas = [Receta(fila['id'], fila['titulo'], fila['descripcion'], fila['ingredientes'], fila['pasos']).a_json() for fila in filas]
        return recetas
    except Exception as e:
        cerrar_conexion(conexion)
        raise e