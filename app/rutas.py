from flask import Blueprint, jsonify, request
from servicios.operaciones_recetas import agregar_receta, obtener_todas_recetas

rutas = Blueprint('rutas', __name__)

@rutas.route('/recetas', methods=['POST'])
def crear_receta():
    """Endpoint para agregar una nueva receta."""
    datos = request.json
    titulo = datos.get('titulo')
    descripcion = datos.get('descripcion')
    ingredientes = datos.get('ingredientes')
    pasos = datos.get('pasos')

    try:
        receta_id = agregar_receta(titulo, descripcion, ingredientes, pasos)
        return jsonify({'mensaje': 'Receta agregada correctamente', 'id_receta': receta_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@rutas.route('/recetas', methods=['GET'])
def obtener_recetas():
    """Endpoint para obtener todas las recetas."""
    try:
        recetas = obtener_todas_recetas()
        return jsonify({'recetas': recetas}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500