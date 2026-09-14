from datetime import date

from persistent import Persistent
from persistent.list import PersistentList


class Venta(Persistent):
    """Representa una venta realizada en la tienda."""

    def __init__(self, id_venta, cliente):
        """Inicializa una venta."""

        self.id_venta = id_venta
        self.fecha = date.today()
        self.cliente = cliente
        self.detalles = PersistentList()

    def agregar_producto(self, detalle):
        """Agrega un detalle de producto a la venta."""

        self.detalles.append(detalle)

    def calcular_subtotal(self):
        """Calcula el subtotal de la venta."""

        return sum(
            detalle.calcular_importe()
            for detalle in self.detalles
        )

    def calcular_total(self):
        """Calcula el total de la venta."""

        return self.calcular_subtotal()

    def consultar_productos(self):
        """Obtiene los productos incluidos en la venta."""

        return [
            detalle.producto
            for detalle in self.detalles
        ]