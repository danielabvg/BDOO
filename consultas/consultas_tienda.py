from datetime import date


def todos_los_productos(root):
    """Devuelve todos los productos registrados."""

    return list(root.productos.values())


def productos_precio_mayor(root, cantidad):
    """Devuelve productos con precio superior al indicado."""

    return [
        producto
        for producto in root.productos.values()
        if producto.precio > cantidad
    ]


def productos_disponibles(root):
    """Devuelve productos que tienen existencias."""

    return [
        producto
        for producto in root.productos.values()
        if producto.verificar_disponibilidad()
    ]


def productos_bajo_stock(root, limite):
    """Devuelve productos por debajo del límite de existencias."""

    return [
        producto
        for producto in root.productos.values()
        if producto.existencias < limite
    ]


def productos_de_proveedor(proveedor):
    """Devuelve los productos de un proveedor."""

    return proveedor.consultar_productos()


def total_ventas(root):
    """Calcula el total de todas las ventas registradas."""

    return sum(
        venta.calcular_total()
        for venta in root.ventas.values()
    )


def reporte_venta_diaria(root, fecha=None):
    """Genera el reporte de ventas de una fecha determinada."""

    if fecha is None:
        fecha = date.today()

    ventas_del_dia = [
        venta
        for venta in root.ventas.values()
        if venta.fecha == fecha
    ]

    total = sum(
        venta.calcular_total()
        for venta in ventas_del_dia
    )

    return {
        "fecha": fecha,
        "ventas_realizadas": len(ventas_del_dia),
        "total_vendido": total
    }