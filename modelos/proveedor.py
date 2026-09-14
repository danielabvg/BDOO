from persistent import Persistent
from persistent.list import PersistentList


class Proveedor(Persistent):
    """Representa un proveedor de productos."""

    def __init__(
        self,
        id_proveedor,
        nombre,
        telefono,
        correo
    ):
        """Inicializa un proveedor."""

        if not nombre:
            raise ValueError(
                "El nombre del proveedor es obligatorio."
            )

        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.productos = PersistentList()

    def agregar_producto(self, producto):
        """Agrega un producto al catálogo del proveedor."""

        if producto not in self.productos:
            self.productos.append(producto)

    def consultar_productos(self):
        """Devuelve los productos proporcionados."""

        return self.productos