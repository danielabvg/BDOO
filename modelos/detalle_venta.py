from persistent import Persistent


class DetalleVenta(Persistent):
    """Representa un producto dentro de una venta."""

    def __init__(self, id_detalle, producto, cantidad):
        """Inicializa un detalle de venta."""

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self.id_detalle = id_detalle
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio

    def calcular_importe(self):
        """Calcula el importe del detalle."""

        return self.cantidad * self.precio_unitario