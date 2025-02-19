DROP DATABASE IF EXISTS recetas;
CREATE DATABASE recetas;
USE recetas;

CREATE TABLE recetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    receta VARCHAR(255) NOT NULL,
    descripcion TEXT
);
