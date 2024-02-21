def calcular_importe_neto(id_venta):
    cursor.execute('SELECT cantidad, precio, tipo FROM Ventas JOIN Libros ON Ventas.id_libro = Libros.id WHERE Ventas.id = ?', (id_venta,))
    venta = cursor.fetchone()
    cantidad = venta[0]
    precio = venta[1]
    tipo = venta[2]
    importe_bruto = cantidad * precio
    porcentaje_descuento = 0
    if cantidad <= 2:
        if tipo == 1:
            porcentaje_descuento = 0.05
        elif tipo == 2:
            porcentaje_descuento = 0.08
        elif tipo == 3:
            porcentaje_descuento = 0.09
        else:
            porcentaje_descuento = 0.02
    elif cantidad <= 6:
        if tipo == 1:
            porcentaje_descuento = 0.06
        elif tipo == 2:
            porcentaje_descuento = 0.16
        elif tipo == 3:
            porcentaje_descuento = 0.18
        else:
            porcentaje_descuento = 0.02
    else:
        if tipo == 1:
            porcentaje_descuento = 0.08
        elif tipo == 2:
            porcentaje_descuento = 0.32
        elif tipo == 3:
            porcentaje_descuento = 0.36
        else:
            porcentaje_descuento = 0.04
    monto_descuento = importe_bruto * porcentaje_descuento
    importe_neto = importe_bruto - monto_descuento
    return importe_neto