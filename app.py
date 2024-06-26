from flask import Flask, jsonify, request
from Modelos import Config, crearConexion, cerrarConexion, Receta

app= Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    conexion= crearConexion()
    if conexion is None or not conexion.is_connected():
        return "Error al conectar a la base de datos", 500
    cerrarConexion(conexion)
    return 'Conexion exitosa a la base de datos MySQL'

if __name__ == '__main__':
    app.run(debug=True)