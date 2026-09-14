from persistent import Persistent


class Producto(Persistent):
    """Representa un producto disponible en la tienda."""

    def __init__(
        self,
        codigo,
        nombre,
        descripcion,
        precio,
        existencias
    ):
        """Inicializa un producto."""

        if not codigo:
            raise ValueError("El código del producto es obligatorio.")

        if not nombre:
            raise ValueError("El nombre del producto es obligatorio.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if existencias < 0:
            raise ValueError(
                "Las existencias no pueden ser negativas."
            )

        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.categoria = None

    def incrementar_existencias(self, cantidad):
        """Incrementa la cantidad disponible del producto."""

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self.existencias += cantidad

    def disminuir_existencias(self, cantidad):
        """Disminuye las existencias si hay suficiente inventario."""

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        if cantidad > self.existencias:
            raise ValueError(
                "No hay suficientes existencias."
            )

        self.existencias -= cantidad

    def verificar_disponibilidad(self):
        """Indica si el producto tiene existencias."""

        return self.existencias > 0

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""

        if nuevo_precio <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        self.precio = nuevo_precio