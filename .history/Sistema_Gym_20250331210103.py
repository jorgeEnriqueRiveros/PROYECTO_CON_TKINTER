from abc import ABC, abstractmethod
from pool_conexion import Conexion
from datetime import date

# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, apellido, telefono, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo = correo

    @abstractmethod
    def guardar(self):
        pass

# Clase Cliente
class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, correo, membresia, id_cliente=None):
        super().__init__(nombre, apellido, telefono, correo)
        self.__id_cliente = id_cliente
        self.__membresia = membresia

    def guardar(self):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO clientes (nombre, apellido, telefono, correo, membresia) VALUES (%s, %s, %s, %s, %s)"
            valores = (self.__nombre, self.__apellido, self.__telefono, self.__correo, self.__membresia)
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
        return f"ID Cliente: {self.__id_cliente}, Nombre: {self.__nombre} {self.__apellido}, Teléfono: {self.__telefono}, Correo: {self.__correo}, Membresía: {self.__membresia}"

# Clase Producto
class Producto:
    def __init__(self, nombre_prodto, precio_unid, id_producto=None):
        self.__id_producto = id_producto
        self.__nombre_prodto = nombre_prodto
        self.__precio_unid = precio_unid

    def guardar_producto(self):
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO productos (nombre_prodto, precio_unid) VALUES (%s, %s)"
            valores = (self.__nombre_prodto, self.__precio_unid)
            cursor.execute(sql, valores)
            conexion.commit()
        conexion.close()

# Clase Compra
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

# Menú interactivo
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar Cliente")
        print("2. Registrar Producto")
        print("3. Realizar Compra")
        print("4. Ver Información del Cliente")
        print("5. Ver Compras de un Cliente")
        print("6. Sumar Valor de Compras de un Cliente")
        print("7. Ordenar Productos Más Vendidos")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            membresia = input("Membresía: ")
            cliente = Cliente(nombre, apellido, telefono, correo, membresia)
            cliente.guardar()
            print("Cliente registrado con éxito.")

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio unitario: "))
            producto = Producto(nombre, precio)
            producto.guardar_producto()
            print("Producto registrado con éxito.")

        elif opcion == "3":
            correo = input("Correo del cliente: ")
            id_cliente = Cliente.obtener_id_cliente(correo)
            if id_cliente:
                forma_pago = input("Forma de pago: ")
                compra = Compra(id_cliente, forma_pago)
                while True:
                    id_producto = int(input("ID del producto: "))
                    cantidad = int(input("Cantidad: "))
                    precio_unid = float(input("Precio unitario: "))
                    compra.agregar_producto(id_producto, cantidad, precio_unid)
                    if input("Agregar otro producto? (s/n): ") != "s":
                        break
                compra.guardar_compra()
                print("Compra registrada con éxito.")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            correo = input("Correo del cliente: ")
            cliente = Cliente.obtener_cliente_por_correo(correo)
            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")

        elif opcion == "5":
            correo = input("Correo del cliente: ")
            id_cliente = Cliente.obtener_id_cliente(correo)
            if id_cliente:
                conexion = Conexion.obtener_conexion()
                with conexion.cursor() as cursor:
                    cursor.execute("""
                        SELECT compras.id_compra, compras.fecha_compra, compras.total_pagado 
                        FROM compras 
                        WHERE compras.id_cliente = %s
                    """, (id_cliente,))
                    compras = cursor.fetchall()
                    if compras:
                        for compra in compras:
                            print(f"Compra ID: {compra[0]}, Fecha: {compra[1]}, Total Pagado: {compra[2]}")
                    else:
                        print("No hay compras registradas para este cliente.")
                conexion.close()
            else:
                print("Cliente no encontrado.")

        elif opcion == "6":
            correo = input("Correo del cliente: ")
            id_cliente = Cliente.obtener_id_cliente(correo)
            if id_cliente:
                conexion = Conexion.obtener_conexion()
                with conexion.cursor() as cursor:
                    cursor.execute("""
                        SELECT SUM(total_pagado) 
                        FROM compras 
                        WHERE id_cliente = %s
                    """, (id_cliente,))
                    total_compras = cursor.fetchone()[0]
                    print(f"Total de compras realizadas por el cliente: {total_compras}")
                conexion.close()
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            conexion = Conexion.obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT productos.nombre_prodto, SUM(detalles_compra.cantidad) AS total_vendido
                    FROM detalles_compra
                    JOIN productos ON productos.id_producto = detalles_compra.id_producto
                    GROUP BY productos.id_producto
                    ORDER BY total_vendido DESC
                """)
                productos_vendidos = cursor.fetchall()
                print("\nProductos más vendidos:")
                for producto in productos_vendidos:
                    print(f"{producto[0]} - Cantidad Vendida: {producto[1]}")
            conexion.close()

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
