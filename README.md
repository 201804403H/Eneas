create database Examen_ISF2
use Examen_ISF2

CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    genero TEXT
);

CREATE TABLE Libros (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    tipo INTEGER,
    precio REAL
);

CREATE TABLE Ventas (
    id INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_libro INTEGER,
    cantidad INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id),
    FOREIGN KEY (id_libro) REFERENCES Libros(id)
);
