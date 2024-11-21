DROP DATABASE IF EXISTS centro_deportivo;
CREATE DATABASE centro_deportivo;
USE centro_deportivo;
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    tipo_membresia VARCHAR(20)
);
CREATE TABLE entrenadores (
    id_entrenador INT AUTO_INCREMENT PRIMARY KEY,
    nombre_entrenador VARCHAR(50),
    especialidad VARCHAR(50)
);
CREATE TABLE actividades (
    id_actividad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_actividad VARCHAR(50),
    horario VARCHAR(50),
    duracion INT,
    id_entrenador INT,
    FOREIGN KEY (id_entrenador) REFERENCES entrenadores(id_entrenador)
);
CREATE TABLE inscripciones (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_actividad INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id_actividad)
);

-- Insertar datos en la tabla clientes
INSERT INTO clientes (nombre, edad, tipo_membresia) VALUES 
('Juan Pérez', 30, 'Premium'),
('Ana Gómez', 25, 'Básica'),
('Carlos Ruiz', 40, 'Estándar');

-- Insertar datos en la tabla entrenadores
INSERT INTO entrenadores (nombre_entrenador, especialidad) VALUES 
('Laura Sánchez', 'Yoga'),
('Miguel Torres', 'CrossFit'),
('Sofía Martínez', 'Pilates');

-- Insertar datos en la tabla actividades
INSERT INTO actividades (nombre_actividad, horario, duracion, id_entrenador) VALUES 
('Clase de Yoga', 'Lunes 10:00 AM', 60, 1),
('Entrenamiento CrossFit', 'Miércoles 6:00 PM', 90, 2),
('Pilates Básico', 'Viernes 9:00 AM', 45, 3);

-- Insertar datos en la tabla inscripciones
INSERT INTO inscripciones (id_cliente, id_actividad) VALUES 
(1, 1),  -- Juan Pérez en Clase de Yoga
(2, 3),  -- Ana Gómez en Pilates Básico
(3, 2);  -- Carlos Ruiz en Entrenamiento CrossFit
