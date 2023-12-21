DROP DATABASE IF EXISTS Lost_in_Space;
CREATE DATABASE IF NOT EXISTS Lost_in_Space;
USE Lost_in_Space;


-- Crear la tabla para almacenar datos de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    passcode VARCHAR (255),
    fecha_nacimiento DATE,
    url_image VARCHAR(255)
);

-- Insertar datos desde el archivo CSV a la tabla de usuarios
COPY usuarios(id, nombre, fecha_nacimiento, url_image)
FROM '/script/db.csv' DELIMITER ',' CSV HEADER;
