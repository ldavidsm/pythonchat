from flask import Flask, request, render_template, jsonify
import json
from flask_cors import CORS

# Creo una nueva aplicación de Flask
aplicacion = Flask(__name__)
# LE añado soporte para aceptar conexiones externas
CORS(aplicacion, resources={r"/*": {"origins": "*"}})

# Creo una lista vacia de  mensajes
mensajes = []
# Ruta que atienda a la raiz del dominio
@aplicacion.route('/')
def inicio():
    return render_template('index.html')
# Ruta a la que se llama para recibir mensajes
@aplicacion.route('/recibe')
def recibe():
    # Traemos los mensajes a la funcion
    global mensajes
    # Devolvemos los mensajes como json
    return json.dumps(mensajes)
# Ruta la que se llama para enviar un mensaje
@aplicacion.route('/envia')
def envia():
    # Traemos los mensajes a la funcion
    global mensajes
    # A los mensajes les añadimos lo que venga por get
    mensaje = {
        "mensaje":request.args.get('mensaje'),
        "usuario":request.args.get('usuario')
        }
    if mensaje:
        mensajes.append(mensaje)
        return jsonify({"success": True, "message": "Mensaje añadido"})
    else:
        return jsonify({"success": False, "error": "Parámetro 'mensaje' no proporcionado"}), 400
    return True

if __name__ == '__main__':
    aplicacion.run(debug=True, host='localhost', port=3000)