from flask import Flask
from config.configuracion import Configuracion
from app.rutas import rutas

def crear_app():
    app = Flask(__name__)
    app.config.from_object(Configuracion)
    
    # Registrar Blueprints
    app.register_blueprint(rutas)
    
    return app