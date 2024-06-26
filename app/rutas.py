from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from servicios.operaciones_recetas import agregar_receta, obtener_todas_recetas

rutas = Blueprint('rutas', __name__)

@rutas.route('/')
def index():
    """Muestra la página principal con todas las recetas."""
    recetas = obtener_todas_recetas()
    return render_template('index.html', recetas=recetas)

@rutas.route('/recetas', methods=['POST'])
def crear_receta():
    """Endpoint para agregar una nueva receta."""
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    ingredientes = request.form['ingredientes']
    pasos = request.form['pasos']

    try:
        agregar_receta(titulo, descripcion, ingredientes, pasos)
        return redirect(url_for('rutas.index'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@rutas.route('/agregar_receta')
def agregar_receta_form():
    """Muestra el formulario para agregar una nueva receta."""
    return render_template('agregar_receta.html')