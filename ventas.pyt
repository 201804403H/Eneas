import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('ventas.db')
cursor = conn.cursor()

# Registrar un cliente
def registrar_cliente(nombre, genero):
    cursor.execute('INSERT INTO Clientes (nombre, genero) VALUES (?, ?)', (nombre, genero))
    conn.commit()

# Registrar un libro
def registrar_libro(titulo, tipo, precio):
    cursor.execute('INSERT INTO Libros (titulo, tipo, precio) VALUES (?, ?, ?)', (titulo, tipo, precio))
    conn.commit()

# Registrar una venta
def registrar_venta(id_cliente, id_libro, cantidad):
    cursor.execute('INSERT INTO Ventas (id_cliente, id_libro, cantidad) VALUES (?, ?, ?)', (id_cliente, id_libro, cantidad))
    conn.commit()

# Calcular el importe neto de una venta
def calcular_importe_neto(id_venta):
    cursor.execute('SELECT cantidad, precio FROM Ventas JOIN Libros ON Ventas.id_libro = Libros.id WHERE Ventas.id = ?', (id_venta,))
    venta = cursor.fetchone()
    cantidad = venta[0]
    precio = venta[1]
    importe_bruto = cantidad * precio
    porcentaje_descuento = 0
    if cantidad <= 2:
        porcentaje_descuento = 0.05
    elif cantidad <= 6:
        porcentaje_descuento = 0.06
    else:
        porcentaje_descuento = 0.08
    monto_descuento = importe_bruto * porcentaje_descuento
    importe_neto = importe_bruto - monto_descuento
    return importe_neto

# Ejemplo de uso
registrar_cliente('Juan Perez', 'M')
registrar_libro('El principito', 1, 90.00)
registrar_venta(1, 1, 3)
importe_neto = calcular_importe_neto(1)
print(importe_neto)