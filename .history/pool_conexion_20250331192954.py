import mysql.connector
from mysql.connector import pooling

class Conexion:
    _DATABASE = 'gym_db'
    _USER = 'root'  # Cambia esto si usas otro usuario
    _PASSWORD = 'tu_contraseña'  # Cambia esto por tu contraseña de MySQL
    _HOST = 'localhost'
    _POOL_SIZE = 5
    _pool = None  # Inicializamos el pool como None

    @classmethod
    def inicializar_pool(cls):
        """Inicializa el pool de conexiones si aún no ha sido creado."""
        if cls._pool is None:
            cls._pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=cls._POOL_SIZE,
                host=cls._HOST,
                user=cls._USER,
                password=cls._PASSWORD,
                database=cls._DATABASE
            )

    @classmethod
    def obtener_conexion(cls):
        """Obtiene una conexión del pool."""
        if cls._pool is None:
            cls.inicializar_pool()  # Asegura que el pool esté inicializado antes de obtener la conexión
        return cls._pool.get_connection()
