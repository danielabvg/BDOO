# BDOO - Tienda La Económica

Sistema modular desarrollado en Python y ZODB para administrar productos, proveedores, clientes y ventas mediante una Base de Datos Orientada a Objetos.

## Estructura

- `modelos/` - Clases y objetos del sistema.
- `persistencia/` - Conexión y almacenamiento mediante ZODB.
- `negocio/` - Lógica de negocio y operaciones CRUD.
- `consultas/` - Consultas de información.
- `main.py` - Punto de entrada de la aplicación.

## Funcionalidades

- Alta, consulta, modificación y eliminación de productos.
- Registro de ventas.
- Actualización de inventario.
- Cálculo de totales.
- Consultas de productos.
- Reporte de venta total diaria.
- Persistencia de objetos mediante ZODB.

## Instalación

```bash
pip install -r requirements.txt