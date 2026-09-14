from modelos.categoria import Categoria
from modelos.cliente import Cliente
from modelos.producto import Producto
from modelos.proveedor import Proveedor

from persistencia.base_datos import BaseDatos

from negocio.tienda_service import TiendaService

from consultas.consultas_tienda import (
    todos_los_productos,
    productos_precio_mayor,
    productos_disponibles,
    productos_bajo_stock,
    productos_de_proveedor,
    total_ventas,
    reporte_venta_diaria
)


def crear_datos_iniciales(base_datos):
    """Crea los datos iniciales de la tienda."""

    root = base_datos.root

    if root.productos:
        return

    bebidas = Categoria(
        1,
        "Bebidas",
        "Productos para beber"
    )

    limpieza = Categoria(
        2,
        "Limpieza",
        "Productos de limpieza"
    )

    root.categorias[1] = bebidas
    root.categorias[2] = limpieza

    producto_coca = Producto(
        "P001",
        "Coca-Cola",
        "Refresco",
        25.0,
        20
    )

    producto_jabon = Producto(
        "P002",
        "Jabón",
        "Jabón para limpieza",
        35.0,
        10
    )

    producto_agua = Producto(
        "P003",
        "Agua",
        "Agua embotellada",
        15.0,
        30
    )

    bebidas.agregar_producto(producto_coca)
    limpieza.agregar_producto(producto_jabon)
    bebidas.agregar_producto(producto_agua)

    root.productos["P001"] = producto_coca
    root.productos["P002"] = producto_jabon
    root.productos["P003"] = producto_agua

    proveedor = Proveedor(
        1,
        "Distribuidora La Central",
        "2281234567",
        "central@gmail.com"
    )

    proveedor.agregar_producto(producto_coca)
    proveedor.agregar_producto(producto_agua)

    root.proveedores[1] = proveedor

    cliente = Cliente(
        1,
        "Daniela",
        "2289876543",
        "daniela@gmail.com"
    )

    root.clientes[1] = cliente

    base_datos.guardar()

    print("Objetos iniciales guardados en ZODB.")


def ejecutar_pruebas():
    """Ejecuta las operaciones principales del sistema."""

    base_datos = BaseDatos()

    try:
        base_datos.abrir()

        crear_datos_iniciales(base_datos)

        servicio = TiendaService(
            base_datos.root,
            base_datos
        )

        root = base_datos.root

        producto_coca = root.productos["P001"]
        proveedor = root.proveedores[1]
        cliente = root.clientes[1]

        # =================================================
        # ALTA
        # =================================================

        print("\n===== ALTA DE PRODUCTO =====")

        producto_nuevo = Producto(
            "P004",
            "Shampoo",
            "Shampoo para cabello",
            50.0,
            8
        )

        try:
            servicio.registrar_producto(producto_nuevo)
            print("Producto agregado correctamente.")
            print("Producto P004 agregado.")
        except ValueError as error:
            print(f"No se pudo agregar: {error}")

        # =================================================
        # CONSULTA
        # =================================================

        print("\n===== CONSULTA DE PRODUCTO =====")

        producto_consultado = servicio.consultar_producto(
            "P004"
        )

        if producto_consultado:
            print(
                f"{producto_consultado.codigo} - "
                f"{producto_consultado.nombre} - "
                f"$ {producto_consultado.precio}"
            )

        # =================================================
        # MODIFICACIÓN
        # =================================================

        print("\n===== MODIFICACIÓN DE PRODUCTO =====")

        try:
            print(
                "Precio anterior:",
                producto_consultado.precio
            )

            servicio.modificar_producto(
                "P004",
                55.0
            )

            print(
                "Precio nuevo:",
                producto_consultado.precio
            )

        except ValueError as error:
            print(f"Error: {error}")

        # =================================================
        # ELIMINACIÓN
        # =================================================

        print("\n===== ELIMINACIÓN DE PRODUCTO =====")

        try:
            servicio.eliminar_producto("P004")
            print("Producto eliminado correctamente.")
        except ValueError as error:
            print(f"Error: {error}")

        # =================================================
        # TODOS LOS PRODUCTOS
        # =================================================

        print("\n===== TODOS LOS PRODUCTOS =====")

        for producto in todos_los_productos(root):
            print(
                f"{producto.codigo} - "
                f"{producto.nombre} - "
                f"$ {producto.precio} - "
                f"Existencias: {producto.existencias}"
            )

        # =================================================
        # PRECIO MAYOR
        # =================================================

        print(
            "\n===== PRODUCTOS CON PRECIO MAYOR A $20 ====="
        )

        for producto in productos_precio_mayor(root, 20):
            print(
                f"{producto.nombre} - "
                f"$ {producto.precio}"
            )

        # =================================================
        # DISPONIBLES
        # =================================================

        print("\n===== PRODUCTOS DISPONIBLES =====")

        for producto in productos_disponibles(root):
            print(
                f"{producto.nombre} - "
                f"Existencias: {producto.existencias}"
            )

        # =================================================
        # BAJO STOCK
        # =================================================

        print(
            "\n===== PRODUCTOS CON MENOS DE "
            "15 EXISTENCIAS ====="
        )

        for producto in productos_bajo_stock(root, 15):
            print(
                f"{producto.nombre} - "
                f"Existencias: {producto.existencias}"
            )

        # =================================================
        # PROVEEDOR
        # =================================================

        print(
            f"\n===== PRODUCTOS DE "
            f"{proveedor.nombre} ====="
        )

        for producto in productos_de_proveedor(proveedor):
            print(producto.nombre)

        # =================================================
        # VENTA
        # =================================================

        print("\n===== REGISTRANDO VENTA =====")

        try:
            venta = servicio.registrar_venta(
                cliente,
                producto_coca,
                2
            )

            print("Venta registrada correctamente.")
            print("ID de venta:", venta.id_venta)
            print("Producto:", producto_coca.nombre)
            print("Cantidad: 2")
            print(
                "Total: $",
                servicio.calcular_total_venta(venta)
            )

        except ValueError as error:
            print(f"No se pudo registrar la venta: {error}")

        # =================================================
        # TOTAL DE VENTAS
        # =================================================

        print("\n===== TOTAL DE VENTAS =====")

        print(
            "Total obtenido: $",
            total_ventas(root)
        )

        # =================================================
        # REPORTE DIARIO
        # =================================================

        print(
            "\n===== REPORTE DE VENTA TOTAL DIARIA ====="
        )

        reporte = reporte_venta_diaria(root)

        print(
            "Fecha:",
            reporte["fecha"].strftime("%d/%m/%Y")
        )

        print(
            "Ventas realizadas:",
            reporte["ventas_realizadas"]
        )

        print(
            "Total vendido: $",
            reporte["total_vendido"]
        )

        # =================================================
        # INVENTARIO
        # =================================================

        print("\n===== INCREMENTAR EXISTENCIAS =====")

        print(
            "Existencias anteriores:",
            producto_coca.existencias
        )

        servicio.incrementar_inventario(
            "P001",
            5
        )

        print(
            "Existencias nuevas:",
            producto_coca.existencias
        )

        # =================================================
        # PERSISTENCIA
        # =================================================

        print("\n===== COMPROBANDO PERSISTENCIA =====")

    except Exception as error:
        print(f"\nError inesperado: {error}")

    finally:
        base_datos.cerrar()

    print("Base de datos cerrada.")
    print("\nVolviendo a abrir la base de datos...")

    # =====================================================
    # VOLVER A ABRIR
    # =====================================================

    segunda_conexion = BaseDatos()

    try:
        segunda_conexion.abrir()

        producto_recuperado = (
            segunda_conexion.root.productos["P001"]
        )

        print(
            "Producto recuperado:",
            producto_recuperado.nombre
        )

        print(
            "Precio:",
            producto_recuperado.precio
        )

        print(
            "Existencias:",
            producto_recuperado.existencias
        )

        print(
            "\nLa información continúa "
            "almacenada correctamente."
        )

    finally:
        segunda_conexion.cerrar()

    print("\nPrograma finalizado.")


def main():
    """Punto de entrada de la aplicación."""

    ejecutar_pruebas()


if __name__ == "__main__":
    main()