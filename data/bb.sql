-- Crear la tabla para almacenar datos de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    fecha_nacimiento DATE,
    url_imagen VARCHAR(255)
);

-- Insertar datos desde el archivo CSV a la tabla de usuarios
COPY usuarios(nombre, fecha_nacimiento, url_imagen)
FROM '/data/db.csv' DELIMITER ',' CSV HEADER;
