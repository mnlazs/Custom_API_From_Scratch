from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import csv
import requests
from datetime import datetime
import mysql.connector


app = Flask(__name__)
CORS(app, resources={r"/obtener_imagen": {"origins": "*"}})
app.static_folder = 'static'

def get_db_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="12345678",
        database="Lost_in_Space"
    )
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tabla', methods=['POST'])
def insert_user():
    try:
        data = request.json  # Usa request.json en lugar de request.data
        conn = get_db_connection()
        cursor = conn.cursor()

        # Utiliza parámetros de consulta para evitar la inyección de SQL
        cursor.execute("INSERT INTO usuarios (nombre, fecha_nacimiento, url_image) VALUES (%s, %s, %s)",
                (data.get('name'), data.get('nacimiento'), data.get('url')))

        conn.commit()  # Asegúrate de hacer commit después de la inserción

        cursor.close()
        conn.close()

        return jsonify({'message': 'Usuario insertado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})


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
    try:
        print ('obtener imagen')
        response = requests.get(url)
        response.raise_for_status() # Esto lanzará un error si la solicitud falla
        data = response.json()
        imagen = data.get('url')
        print ('inside of obtener_image: ', imagen)
        
        return (imagen) 
    except requests.RequestException as e:
        print(f"Error al obtener la imagen: {e}")
        return None
    
    # Comprobar si 'url' está en la respuesta
    imagen_url = data.get('url')
    if imagen_url:
        return imagen_url
    else:
        # Manejar el caso en que 'url' no esté disponible
        # Devolver None o un mensaje de error
        return None

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
@app.route('/obtener_imagen_actual', methods=['GET','POST'])
@cross_origin()
def obtener_imagen_actual():
    datos = cargar_datos()
    nombre = request.json.get('nombre')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    data = request.json
    print(data)
        
    if nombre is None or fecha_nacimiento is None:
    # Maneja el caso donde falta información
        response = jsonify({'error': 'Falta nombre o fecha de nacimiento'}), 400
        return response

    # Si no se proporciona una fecha de nacimiento, usar la fecha actual
    if not fecha_nacimiento:
        url_imagen = obtener_imagen_actual()
    else:
    # Lógica para determinar la fecha correspondiente al día de nacimiento
        # fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, '%y-%m-%d')
        # fecha = fecha_nacimiento_dt.strftime('%y-%m-%d')

        # Obtener la URL de la imagen del universo para la fecha de nacimiento
        url_imagen = obtener_imagen(fecha_nacimiento)

    # Actualizar datos del usuario en el archivo CSV
    actualizar_datos_csv(nombre, fecha_nacimiento, url_imagen)

    # Responder con la URL de la imagen
    return jsonify({'nombre': nombre, 'url_imagen': url_imagen})


if __name__ == '__main__':
    app.run(debug=True, port=8000)