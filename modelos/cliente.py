from persistent import Persistent
from persistent.list import PersistentList


class Cliente(Persistent):
    """Representa un cliente de la tienda."""

    def __init__(
        self,
        id_cliente,
        nombre,
        telefono,
        correo
    ):
        """Inicializa un cliente."""

        if not nombre:
            raise ValueError(
                "El nombre del cliente es obligatorio."
            )

        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.ventas = PersistentList()

    def consultar_ventas(self):
        """Devuelve las ventas realizadas por el cliente."""

        return self.ventas