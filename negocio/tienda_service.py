from modelos.detalle_venta import DetalleVenta
from modelos.producto import Producto
from modelos.venta import Venta


class TiendaService:
    """Contiene la lógica de negocio de la tienda."""

    def __init__(self, root, base_datos):
        """Inicializa el servicio de la tienda."""

        self.root = root
        self.base_datos = base_datos

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def registrar_producto(self, producto):
        """Registra un producto en la base de datos."""

        if producto.codigo in self.root.productos:
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        self.root.productos[producto.codigo] = producto
        self.base_datos.guardar()

    def consultar_producto(self, codigo):
        """Busca un producto mediante su código."""

        return self.root.productos.get(codigo)

    def modificar_producto(self, codigo, nuevo_precio):
        """Modifica el precio de un producto."""

        producto = self.consultar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado."
            )

        producto.actualizar_precio(nuevo_precio)
        self.base_datos.guardar()

        return producto

    def eliminar_producto(self, codigo):
        """Elimina un producto de la base de datos."""

        if codigo not in self.root.productos:
            raise ValueError(
                "Producto no encontrado."
            )

        del self.root.productos[codigo]
        self.base_datos.guardar()

    # =====================================================
    # INVENTARIO
    # =====================================================

    def incrementar_inventario(self, codigo, cantidad):
        """Incrementa las existencias de un producto."""

        producto = self.consultar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado."
            )

        producto.incrementar_existencias(cantidad)
        self.base_datos.guardar()

        return producto

    def disminuir_inventario(self, codigo, cantidad):
        """Disminuye las existencias de un producto."""

        producto = self.consultar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado."
            )

        producto.disminuir_existencias(cantidad)
        self.base_datos.guardar()

        return producto

    # =====================================================
    # VENTAS
    # =====================================================

    def _nuevo_id_venta(self):
        """Genera un identificador único para una venta."""

        if not self.root.ventas:
            return 1

        return max(self.root.ventas.keys()) + 1

    def registrar_venta(self, cliente, producto, cantidad):
        """Registra una nueva venta."""

        producto.disminuir_existencias(cantidad)

        id_venta = self._nuevo_id_venta()

        venta = Venta(
            id_venta,
            cliente
        )

        detalle = DetalleVenta(
            id_venta,
            producto,
            cantidad
        )

        venta.agregar_producto(detalle)

        cliente.ventas.append(venta)
        self.root.ventas[id_venta] = venta

        self.base_datos.guardar()

        return venta

    def calcular_total_venta(self, venta):
        """Obtiene el total de una venta."""

        return venta.calcular_total()