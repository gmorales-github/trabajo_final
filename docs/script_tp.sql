-- Paso 1: Crear la base de datos
CREATE DATABASE IF NOT EXISTS dbtienda;
USE dbtienda;

-- Paso 2: Crear las tablas

-- Crear la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    admin BOOLEAN NOT NULL
);

-- Crear la tabla marcas
CREATE TABLE IF NOT EXISTS marcas (
    id_marca INT AUTO_INCREMENT PRIMARY KEY,
    nombre_marca VARCHAR(50) NOT NULL
);

-- Crear la tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT,
    stock INT NOT NULL,
    id_marca INT,
    FOREIGN KEY (id_marca) REFERENCES marcas(id_marca)
);

-- Crear la tabla ventas
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    fecha DATE NOT NULL,
    total_final DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- Crear la tabla detalle_venta
CREATE TABLE IF NOT EXISTS detalle_venta (
    id_detalle_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    total_por_producto DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Paso 3: Insertar datos iniciales

-- Insertar datos en la tabla usuarios
INSERT INTO usuarios (nombre_usuario, contrasenia, correo, telefono, admin) VALUES
('admin1', 'adminpass1', 'admin1@tienda.com', '1111111111', TRUE),
('usuario1', 'userpass1', 'user1@tienda.com', '2222222222', FALSE),
('usuario2', 'userpass2', 'user2@tienda.com', '3333333333', FALSE);

-- Insertar datos en la tabla marcas
INSERT INTO marcas (nombre_marca) VALUES
('Apple'),
('Samsung'),
('Sony'),
('Dell'),
('HP');

-- Insertar datos en la tabla productos
INSERT INTO productos (nombre_producto, precio, descripcion, stock, id_marca) VALUES
('iPhone 14', 500000.00, 'Smartphone de última generación', 15, 1),
('Samsung Galaxy S22', 450000.00, 'Smartphone Android de alta gama', 20, 2),
('Sony PlayStation 5', 600000.00, 'Consola de videojuegos de nueva generación', 10, 3),
('Dell XPS 13', 700000.00, 'Laptop ultradelgada y potente', 8, 4),
('HP Spectre x360', 650000.00, 'Laptop convertible con pantalla táctil', 12, 5);

-- Insertar datos en la tabla ventas
INSERT INTO ventas (id_usuario, fecha, total_final) VALUES
(1, '2024-06-01', 500000.00),
(2, '2024-06-02', 450000.00),
(3, '2024-06-03', 600000.00);

-- Insertar datos en la tabla detalle_venta
INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio, total_por_producto) VALUES
(1, 1, 1, 500000.00, 500000.00),
(2, 2, 1, 450000.00, 450000.00),
(3, 3, 1, 600000.00, 600000.00);