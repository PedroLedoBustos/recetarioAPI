# Contiene las operaciones CRUD
from Modelos import Receta,crearConexion, cerrarConexion

def agregarReceta(titulo, descripcion, ingredientes, pasos):
    conexion= crearConexion()
    cursor= conexion.cursor()

    try:
        cursor.execute('INSERT INTO recetas (titulo, descripcion, ingredientes, pasos) VALUES (%s, %s, %s, %s)', (titulo, descripcion,ingredientes,pasos))
        conexion.commit()
        recetaId= cursor.lastrowid
        cerrarConexion(conexion)
        return f'La receta con ID: {recetaId} y titulo {titulo} ha sido agregada con éxito'
    except Exception as e:
        cerrarConexion(conexion)
        raise e

