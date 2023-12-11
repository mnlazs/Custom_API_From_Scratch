window.addEventListener('load',obtenerDatos);

function obtenerDatos () {

    const NASA_key = 'GYb0xavvxZOEehQCaSx4YG1wZ9aXoNpdz99nlWqf'
    const ruta = `https://api.nasa.gov/planetary/apod?api_key=${NASA_key}`;

    fectch(ruta)
    .then(respuesta => respuesta.json())
    .then(resultado => mostrarDatos(resultado))
}

function mostrarDatos({date, explanation, media_type, title, url }) {

    const titulo = document.querySelector('#titulo');
    titulo.innerHTML = title;
    const fecha = document.querySelector('#fecha');
    fecha.innerHTML = date;
    const descripcion = document.querySelector('#descripcion');
    descripcion.innerHTML = explanation;
    
    const multimedia = document.querySelector('#c_multimedia');
    if(media_type == 'video') {
        multimedia.innerHTML = `
        <iframe class="embed-responsive-item" src="${url}"></iframe>`
    }else{
    multimedia.innerHTML = `
    <img src="${url}" class="img-fluid" alt="${url}">
    `
      }


}
