DROP DATABASE IF EXISTS HITO_PROG;
CREATE DATABASE HITO_PROG;
USE HITO_PROG;


CREATE TABLE producto (
    idproducto int auto_increment primary key,
    nombre varchar(150),
    medida varchar(100),
    precio int,
    stock int
);

CREATE TABLE cliente (
    idcliente INT auto_increment primary key,
    nombre varchar(100),
    direccion varchar(200),
    tlf int
);


CREATE TABLE pedido (
    idpedido int auto_increment primary key,
    idcliente int,
	fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    foreign key (idcliente) references cliente(idcliente)
);

CREATE TABLE detalle (
	idcliente int,
    idpedido int,
    idproducto int,
    precio float,
    unidades int,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    foreign key (idpedido) references pedido(idpedido),
    foreign key (idproducto) references producto(idproducto),
    foreign key (idcliente) references cliente(idcliente)
);



-- Insertar Producto 1
INSERT INTO producto (nombre, medida, precio, stock) 
VALUES ('Camiseta', 'M', 15, 50);

-- Insertar Producto 2
INSERT INTO producto (nombre, medida, precio, stock) 
VALUES ('Zapatos Deportivos', '42', 45, 30);

-- Insertar Producto 3
INSERT INTO producto (nombre, medida, precio, stock) 
VALUES ('Auriculares Bluetooth', 'Unidad', 25, 100);

-- Insertar Producto 4
INSERT INTO producto (nombre, medida, precio, stock) 
VALUES ('Reloj de Pulsera', 'Unidad', 80, 10);

-- Insertar Producto 5
INSERT INTO producto (nombre, medida, precio, stock) 
VALUES ('Mochila de Viaje', 'Grande', 40, 20);

INSERT INTO cliente (nombre, direccion, tlf) VALUES
('Carlos Sánchez', 'Av. Las Palmas 123', 654321987),
('Lucía Ramírez', 'Calle La Colina 45', 987654321),
('Andrés Pérez', 'Av. Central 67', 123456789),
('Mariana López', 'Calle Bella Vista 89', 456789123),
('Fernando García', 'Pasaje Los Olivos 10', 789123456);


INSERT INTO pedido (idcliente) VALUES
(1), -- Pedido de Carlos Sánchez
(2), -- Pedido de Lucía Ramírez
(3), -- Pedido de Andrés Pérez
(4), -- Pedido de Mariana López
(5); -- Pedido de Fernando García


INSERT INTO detalle (idcliente,idpedido, idproducto, precio, unidades) VALUES
(1,1, 1, 15, 2),      -- Carlos Sánchez compró 2 camisetas sin descuento
(1,1, 3, 25, 1),      -- Carlos Sánchez compró 1 auricular con 5 de descuento
(2,2,2, 45, 1),      -- Lucía Ramírez compró 1 par de zapatos deportivos
(2,2, 5, 40, 2),     -- Lucía Ramírez compró 2 mochilas con 10 de descuento
(3,3, 4, 80, 1),     -- Andrés Pérez compró 1 reloj de pulsera con 15 de descuento
(4,4, 1, 15, 3),      -- Mariana López compró 3 camisetas sin descuento
(4,4, 2, 45, 1),      -- Mariana López compró 1 par de zapatos deportivos
(5,5, 5, 40, 1);      -- Fernando García compró 1 mochila con 5 de descuento


