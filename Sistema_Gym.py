from abc import ABC, abstractmethod
from Pool_Conexion import Conexion
from datetime import date

# Clase abstracta Persona con atributos privados
class Persona(ABC):
    def __init__(self, nombre, apellido, telefono, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo = correo

    # Propiedades para acceder a los atributos privados
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def telefono(self):
        return self.__telefono

    @property
    def correo(self):
        return self.__correo

    @abstractmethod
    def guardar(self):
        pass

# Clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, correo, membresia, id_cliente=None):
        super().__init__(nombre, apellido, telefono, correo)
        self.__id_cliente = id_cliente
        self.__membresia = membresia

    @property
    def membresia(self):
        return self.__membresia

    def guardar(self):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO clientes (nombre, apellido, telefono, correo, membresia) VALUES (%s, %s, %s, %s, %s)"
            # Usamos las propiedades para acceder a los atributos privados de Persona
            valores = (self.nombre, self.apellido, self.telefono, self.correo, self.__membresia)
            cursor.execute(sql, valores)
            conexion.commit()
        conexion.close()

    @classmethod
    def obtener_id_cliente(cls, correo):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_cliente FROM clientes WHERE correo = %s", (correo,))
            resultado = cursor.fetchone()
        conexion.close()
        return resultado[0] if resultado else None

    @classmethod
    def obtener_cliente_por_correo(cls, correo):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes WHERE correo = %s", (correo,))
            resultado = cursor.fetchone()
        conexion.close()
        if resultado:
            return Cliente(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[0])
        return None

    def __str__(self):
        return f"ID Cliente: {self.__id_cliente}, Nombre: {self.nombre} {self.apellido}, Teléfono: {self.telefono}, Correo: {self.correo}, Membresía: {self.__membresia}"

# La clase Producto y Compra se mantienen de forma similar (puedes aplicar la misma lógica con propiedades si fuera necesario)
class Producto:
    def __init__(self, nombre_prodto, precio_unid, id_producto=None):
        self.__id_producto = id_producto
        self.__nombre_prodto = nombre_prodto
        self.__precio_unid = precio_unid

    @property
    def nombre_prodto(self):
        return self.__nombre_prodto

    @property
    def precio_unid(self):
        return self.__precio_unid

    def guardar_producto(self):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO productos (nombre_prodto, precio_unid) VALUES (%s, %s)"
            valores = (self.__nombre_prodto, self.__precio_unid)
            cursor.execute(sql, valores)
            conexion.commit()
        conexion.close()

class Compra:
    def __init__(self, id_cliente, forma_pago, id_compra=None, fecha_compra=None, total_pagado=None):
        self.__id_compra = id_compra
        self.__id_cliente = id_cliente
        self.__fecha_compra = fecha_compra or date.today()
        self.__total_pagado = total_pagado
        self.__forma_pago = forma_pago
        self.__carrito_compras = []

    def agregar_producto(self, id_producto, cantidad, precio_unid):
        self.__carrito_compras.append((id_producto, cantidad, precio_unid))

    def guardar_compra(self):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO compras (id_cliente, fecha_compra, total_pagado, forma_pago) VALUES (%s, %s, NULL, %s)"
            cursor.execute(sql, (self.__id_cliente, self.__fecha_compra, self.__forma_pago))
            self.__id_compra = cursor.lastrowid

            for item in self.__carrito_compras:
                sql_detalle = "INSERT INTO detalles_compra (id_compra, id_producto, cantidad, precio_final) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_detalle, (self.__id_compra, *item))
            conexion.commit()
        conexion.close()
