# Lost in Space: Universe Image Fetcher 🌌🚀

## Description
"Lost in Space" is a web application that connects you with the universe. 🌟 It fetches images from NASA's API based on your birth date and saves user data in a local CSV file.

## Key Features
- **Image Fetching**: Get images of the universe for specific dates. 📅🌠
- **User Data Management**: Store user details in a CSV file. 📝👤
- **Web Interface**: Easy-to-use interface for entering data and viewing images. 🖥️👀
- **CORS Enabled**: Access the API from different domains. 🌐🔗

## Setup and Installation
1. Clone the repository.
2. Install dependencies: pip install -r requirements.txt.
3. Run the Flask app: python app.py.
4. Open the webpage in a browser and start exploring the universe! 🌍➡️🌌

## How It Works
- **User Data Input**: Users enter their name and birth date on the web interface.
- **Image Retrieval**: The app requests an image from NASA's API based on the provided date. 📡🛰️
- **Data Storage**: User data along with the image URL is stored in a local CSV file. 🗃️🔒
- **Display Image**: The image is then displayed on the user's screen. 🖼️👁️

1. **User Data Input**
   Users enter their name and birth date on the web interface.

   ```javascript
   const nombre = document.getElementById('nombre').value;
   const fechaNacimiento = document.getElementById('fechaNacimiento').value;


2. **Image Retrieval**
The app requests an image from NASA's API using the provided date.

    ```python
    def obtener_imagen(fecha):
        # ... API request logic ...
        imagen = data.get('url')
        return imagen

3. **Data Storage**
User data along with the image URL is stored in a CSV file.'

    ```python
    def actualizar_datos_csv(nombre, fecha_nacimiento, url_imagen):
        # ... CSV file update logic ...

4. **Display Image**
The image is displayed on the user's screen.

   ```python
    resultadoDiv.innerHTML = `<img src="${data.url_imagen}" alt="Imagen del Universo">`;

  # Endpoint Details
- /: The home route that serves the main page.

   ```python
  @app.route('/')
def home():
    return render_template('index.html')

    
- /tabla: POST endpoint for inserting user data.

 ```python
@app.route('/tabla', methods=['POST'])
def insert_user():
    try:
        data = request.json  # Usa request.json en lugar de request.data
        conn = get_db_connection()
        cursor = conn.cursor()

        # param param pampam
 ```

- /obtener_imagen_actual: GET/POST endpoint for fetching current or specific date universe images.


## Technologies Used

**Flask:** For creating the backend server and API. 🐍
**JavaScrip:t** To handle user interactions on the frontend. 📜
**MySQL:** For database management. 🛢️🔍
**HTML/CSS:** For crafting the web interface. 🎨👩‍💻



## Authors:
* [Dae Thomas](https://github.com/daeshov)
* [Manuel Zambrado](https://github.com/mnlazs)
* [Nikki Alderman](https://github.com/NikkiMerena)


