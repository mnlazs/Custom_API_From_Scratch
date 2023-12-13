document.addEventListener('DOMContentLoaded', function () {
  const formulario = document.getElementById('consultaForm');
  const resultadoDiv = document.getElementById('resultado');

  formulario.addEventListener('submit', function (event) {
      event.preventDefault();

      const nombre = document.getElementById('nombre').value;
      const fechaNacimiento = document.getElementById('fechaNacimiento').value;

        // Enviar solicitud al backend para obtener la imagen del universo del día de la fecha seleccionada
        fetch('/obtener_imagen', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ nombre, fecha_nacimiento: fechaNacimiento }),
      })
      .then(response => response.json())
      .then(data => {
          // Mostrar la imagen en el frontend
          resultadoDiv.innerHTML = `<p>${data.nombre}, aquí está tu imagen del universo:</p><img src="${data.url_imagen}" alt="Imagen del Universo">`;
      })
      .catch(error => console.error('Error:', error));
  });
});
