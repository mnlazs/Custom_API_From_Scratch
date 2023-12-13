from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import csv
import requests
from datetime import datetime

app = Flask(__name__)

# Cargar datos desde el archivo CSV
def cargar_datos():
    datos = []
    with open('tabla.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            datos.append(row)
    return datos

# Obtener la imagen del universo para la fecha actual desde la API de la NASA
def obtener_imagen_actual():
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    return obtener_imagen(fecha_actual)


def obtener_imagen(fecha):
    api_key = 'kpzn2IRF9yVR653LJN6WPZJu7dlGZoqI8BD0gnxd'
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={fecha}'
    response = requests.get(url)
    data = response.json()
    return data['url']

# Actualizar datos del usuario en el archivo CSV
def actualizar_datos_csv(nombre, fecha_nacimiento, url_imagen):
    datos = cargar_datos()

    # Buscar si el usuario ya existe en los datos
    usuario_existente = False
    for usuario in datos:
        if usuario['nombre'] == nombre and usuario['fecha_nacimiento'] == fecha_nacimiento:
            usuario_existente = True
            break

    # Si el usuario no existe, agregarlo al archivo CSV
    if not usuario_existente:
        with open('tabla.csv', 'a', newline='') as csvfile:
            fieldnames = ['nombre', 'fecha_nacimiento', 'url_imagen']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'nombre': nombre, 'fecha_nacimiento': fecha_nacimiento, 'url_imagen': url_imagen})

# Endpoint para obtener la imagen del universo basada en la fecha de nacimiento
@app.route('/obtener_imagen', methods=['POST'])
def obtener_imagen_usuario():
    datos = cargar_datos()
    nombre = request.json['nombre']
    fecha_nacimiento = request.json['fecha_nacimiento']


    # Si no se proporciona una fecha de nacimiento, usar la fecha actual
    if not fecha_nacimiento:
        url_imagen = obtener_imagen_actual()
    else:
    # Lógica para determinar la fecha correspondiente al día de nacimiento
        fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        fecha_nacimiento_str = fecha_nacimiento_dt.strftime('%Y-%m-%d')

        # Obtener la URL de la imagen del universo para la fecha de nacimiento
        url_imagen = obtener_imagen(fecha_nacimiento_str)

    # Actualizar datos del usuario en el archivo CSV
    actualizar_datos_csv(nombre, fecha_nacimiento_str, url_imagen)

    # Responder con la URL de la imagen
    return jsonify({'nombre': nombre, 'url_imagen': url_imagen})

# Route to serve the main page
@app.route('/')
def index():
    # Render the 'index.html' template when accessing the root '/'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
