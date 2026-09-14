import transaction
import ZODB
import ZODB.FileStorage

from persistent.mapping import PersistentMapping


DATABASE_FILE = "datos.fs"


class BaseDatos:
    """Administra la conexión y persistencia mediante ZODB."""

    def __init__(self):
        """Inicializa la conexión con la base de datos."""

        self.storage = ZODB.FileStorage.FileStorage(
            DATABASE_FILE
        )
        self.database = ZODB.DB(self.storage)
        self.connection = None
        self.root = None

    def abrir(self):
        """Abre la conexión y prepara la raíz de ZODB."""

        self.connection = self.database.open()
        self.root = self.connection.root()

        self._inicializar_estructura()

        return self.root

    def _inicializar_estructura(self):
        """Crea las estructuras persistentes necesarias."""

        if not hasattr(self.root, "productos"):
            self.root.productos = PersistentMapping()

        if not hasattr(self.root, "categorias"):
            self.root.categorias = PersistentMapping()

        if not hasattr(self.root, "proveedores"):
            self.root.proveedores = PersistentMapping()

        if not hasattr(self.root, "clientes"):
            self.root.clientes = PersistentMapping()

        if not hasattr(self.root, "ventas"):
            self.root.ventas = PersistentMapping()

        transaction.commit()

    def guardar(self):
        """Confirma la transacción actual."""

        transaction.commit()

    def cerrar(self):
        """Cierra la conexión y el almacenamiento."""

        if self.connection is not None:
            self.connection.close()

        self.database.close()
        self.storage.close()