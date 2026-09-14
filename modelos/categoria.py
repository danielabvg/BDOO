from persistent import Persistent


class Categoria(Persistent):
    """Representa una categoría de productos."""

    def __init__(self, id_categoria, nombre, descripcion):
        """Inicializa una categoría."""

        if not nombre:
            raise ValueError(
                "El nombre de la categoría es obligatorio."
            )

        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion

    def agregar_producto(self, producto):
        """Asocia un producto con esta categoría."""

        producto.categoria = self

    def consultar_productos(self, productos):
        """Obtiene los productos pertenecientes a la categoría."""

        return [
            producto
            for producto in productos.values()
            if producto.categoria == self
        ]