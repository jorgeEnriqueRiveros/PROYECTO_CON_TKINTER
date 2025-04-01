import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Importa las clases y funciones definidas en Sistema_Gym.py
from Sistema_Gym import Cliente, Producto, Compra
from Pool_Conexion import Conexion  # Asegúrate de que este módulo exista y funcione correctamente

# -------------------- Funciones GUI para cada acción --------------------

def registrar_cliente_gui():
    ventana = tk.Toplevel()
    ventana.title("Registrar Cliente")
    ventana.geometry("400x400")
    
    tk.Label(ventana, text="Nombre:").pack(pady=2)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=2)
    
    tk.Label(ventana, text="Apellido:").pack(pady=2)
    entry_apellido = tk.Entry(ventana)
    entry_apellido.pack(pady=2)
    
    tk.Label(ventana, text="Teléfono:").pack(pady=2)
    entry_telefono = tk.Entry(ventana)
    entry_telefono.pack(pady=2)
    
    tk.Label(ventana, text="Correo:").pack(pady=2)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=2)
    
    tk.Label(ventana, text="Membresía:").pack(pady=2)
    entry_membresia = tk.Entry(ventana)
    entry_membresia.pack(pady=2)
    
    def guardar_cliente():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        membresia = entry_membresia.get()
        if nombre and apellido and telefono and correo and membresia:
            cliente = Cliente(nombre, apellido, telefono, correo, membresia)
            try:
                cliente.guardar()
                messagebox.showinfo("Éxito", "Cliente registrado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar cliente:\n{e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    tk.Button(ventana, text="Guardar", command=guardar_cliente).pack(pady=10)

def registrar_producto_gui():
    ventana = tk.Toplevel()
    ventana.title("Registrar Producto")
    ventana.geometry("400x300")
    
    tk.Label(ventana, text="Nombre del Producto:").pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)
    
    tk.Label(ventana, text="Precio Unitario:").pack(pady=5)
    entry_precio = tk.Entry(ventana)
    entry_precio.pack(pady=5)
    
    def guardar_producto():
        nombre = entry_nombre.get()
        try:
            precio = float(entry_precio.get())
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número")
            return
        if nombre:
            producto = Producto(nombre, precio)
            try:
                producto.guardar_producto()
                messagebox.showinfo("Éxito", "Producto registrado correctamente")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar producto:\n{e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    tk.Button(ventana, text="Guardar", command=guardar_producto).pack(pady=10)

def realizar_compra_gui():
    ventana = tk.Toplevel()
    ventana.title("Realizar Compra")
    ventana.geometry("500x500")
    
    tk.Label(ventana, text="Correo del Cliente:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)
    
    tk.Label(ventana, text="Forma de Pago:").pack(pady=5)
    entry_pago = tk.Entry(ventana)
    entry_pago.pack(pady=5)
    
    productos = []  # Lista para almacenar los productos a comprar
    
    frame_producto = tk.Frame(ventana)
    frame_producto.pack(pady=10)
    
    tk.Label(frame_producto, text="ID Producto:").grid(row=0, column=0, padx=5, pady=2)
    entry_id_producto = tk.Entry(frame_producto)
    entry_id_producto.grid(row=0, column=1, padx=5, pady=2)
    
    tk.Label(frame_producto, text="Cantidad:").grid(row=1, column=0, padx=5, pady=2)
    entry_cantidad = tk.Entry(frame_producto)
    entry_cantidad.grid(row=1, column=1, padx=5, pady=2)
    
    tk.Label(frame_producto, text="Precio Unitario:").grid(row=2, column=0, padx=5, pady=2)
    entry_precio = tk.Entry(frame_producto)
    entry_precio.grid(row=2, column=1, padx=5, pady=2)
    
    lista_productos = tk.Listbox(ventana)
    lista_productos.pack(pady=10, fill="both", expand=True)
    
    def agregar_producto():
        try:
            id_producto = int(entry_id_producto.get())
            cantidad = int(entry_cantidad.get())
            precio = float(entry_precio.get())
        except ValueError:
            messagebox.showerror("Error", "Verifica los datos numéricos (ID, cantidad, precio)")
            return
        productos.append((id_producto, cantidad, precio))
        lista_productos.insert(tk.END, f"ID: {id_producto}, Cantidad: {cantidad}, Precio: {precio}")
        # Limpiar entradas
        entry_id_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    
    tk.Button(frame_producto, text="Agregar Producto", command=agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)
    
    def finalizar_compra():
        correo = entry_correo.get()
        forma_pago = entry_pago.get()
        if not correo or not forma_pago:
            messagebox.showerror("Error", "El correo y la forma de pago son obligatorios")
            return
        id_cliente = Cliente.obtener_id_cliente(correo)
        if not id_cliente:
            messagebox.showerror("Error", "Cliente no encontrado")
            return
        compra = Compra(id_cliente, forma_pago)
        for prod in productos:
            compra.agregar_producto(*prod)
        try:
            compra.guardar_compra()
            messagebox.showinfo("Éxito", "Compra registrada correctamente")
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar la compra:\n{e}")
    
    tk.Button(ventana, text="Finalizar Compra", command=finalizar_compra).pack(pady=10)

def ver_info_cliente_gui():
    ventana = tk.Toplevel()
    ventana.title("Ver Información del Cliente")
    ventana.geometry("400x300")
    
    tk.Label(ventana, text="Correo del Cliente:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)
    
    info_text = tk.Text(ventana, height=10, width=50)
    info_text.pack(pady=10)
    
    def buscar_cliente():
        correo = entry_correo.get()
        cliente = Cliente.obtener_cliente_por_correo(correo)
        info_text.delete("1.0", tk.END)
        if cliente:
            info_text.insert(tk.END, str(cliente))
        else:
            messagebox.showerror("Error", "Cliente no encontrado")
    
    tk.Button(ventana, text="Buscar", command=buscar_cliente).pack(pady=5)

def ver_compras_cliente_gui():
    ventana = tk.Toplevel()
    ventana.title("Ver Compras del Cliente")
    ventana.geometry("500x400")
    
    tk.Label(ventana, text="Correo del Cliente:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)
    
    compras_text = tk.Text(ventana, height=15, width=60)
    compras_text.pack(pady=10)
    
    def buscar_compras():
        correo = entry_correo.get()
        id_cliente = Cliente.obtener_id_cliente(correo)
        compras_text.delete("1.0", tk.END)
        if not id_cliente:
            messagebox.showerror("Error", "Cliente no encontrado")
            return
        try:
            conexion = Conexion.obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT id_compra, fecha_compra, total_pagado 
                    FROM compras 
                    WHERE id_cliente = %s
                """, (id_cliente,))
                compras = cursor.fetchall()
            conexion.close()
            if compras:
                for compra in compras:
                    compras_text.insert(tk.END, f"Compra ID: {compra[0]}, Fecha: {compra[1]}, Total Pagado: {compra[2]}\n")
            else:
                compras_text.insert(tk.END, "No hay compras registradas para este cliente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener compras:\n{e}")
    
    tk.Button(ventana, text="Buscar Compras", command=buscar_compras).pack(pady=5)

def sumar_valor_compras_gui():
    ventana = tk.Toplevel()
    ventana.title("Sumar Valor de Compras")
    ventana.geometry("400x300")
    
    tk.Label(ventana, text="Correo del Cliente:").pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)
    
    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack(pady=10)
    
    def sumar_compras():
        correo = entry_correo.get()
        id_cliente = Cliente.obtener_id_cliente(correo)
        if not id_cliente:
            messagebox.showerror("Error", "Cliente no encontrado")
            return
        try:
            conexion = Conexion.obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("SELECT SUM(total_pagado) FROM compras WHERE id_cliente = %s", (id_cliente,))
                total = cursor.fetchone()[0]
            conexion.close()
            resultado_label.config(text=f"Total de compras: {total}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al sumar compras:\n{e}")
    
    tk.Button(ventana, text="Sumar Compras", command=sumar_compras).pack(pady=5)

def ordenar_productos_gui():
    ventana = tk.Toplevel()
    ventana.title("Productos Más Vendidos")
    ventana.geometry("500x400")
    
    productos_text = tk.Text(ventana, height=20, width=60)
    productos_text.pack(pady=10)
    
    try:
        conexion = Conexion.obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT p.nombre_prodto, SUM(dc.cantidad) AS total_vendido
                FROM detalles_compra dc
                JOIN productos p ON p.id_producto = dc.id_producto
                GROUP BY p.id_producto
                ORDER BY total_vendido DESC
            """)
            productos = cursor.fetchall()
        conexion.close()
        if productos:
            for prod in productos:
                productos_text.insert(tk.END, f"{prod[0]} - Cantidad Vendida: {prod[1]}\n")
        else:
            productos_text.insert(tk.END, "No hay datos de ventas.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener productos vendidos:\n{e}")

# -------------------- Funciones de Login y Panel Principal --------------------

def validar_login():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    if usuario == "root" and contraseña == "123456":
        windows.withdraw()  # Oculta la ventana de login
        abrir_panel_consultas()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def abrir_panel_consultas():
    panel = tk.Toplevel()
    panel.title("Panel de Consultas")
    panel.geometry("600x700")
    panel.resizable(0, 0)
    
    # Imagen de fondo para el panel de consultas
    imagen_fondo_panel = ImageTk.PhotoImage(imagen)
    label_fondo_panel = tk.Label(panel, image=imagen_fondo_panel)
    label_fondo_panel.place(x=0, y=0, relwidth=1, relheight=1)
    panel.imagen_fondo_panel = imagen_fondo_panel
    
    frame_menu = tk.Frame(panel, bg="#053A20", bd=2, relief="ridge")
    frame_menu.place(relx=0.5, rely=0.5, anchor="center", width=400, height=600)
    
    tk.Label(frame_menu, text="Menú de Consultas", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    # Lista de botones y funciones asociadas
    botones = [
        ("Registrar Cliente", registrar_cliente_gui),
        ("Registrar Producto", registrar_producto_gui),
        ("Realizar Compra", realizar_compra_gui),
        ("Ver Información Cliente", ver_info_cliente_gui),
        ("Ver Compras Cliente", ver_compras_cliente_gui),
        ("Sumar Valor Compras", sumar_valor_compras_gui),
        ("Ordenar Productos Más Vendidos", ordenar_productos_gui),
        ("Salir", panel.destroy)
    ]
    
    for texto, funcion in botones:
        tk.Button(frame_menu, text=texto, font=("Century Gothic", 12, "bold"),
                  bg="#157347", fg="white", command=funcion).pack(pady=5, fill="x")

# -------------------- Ventana de Login Principal --------------------

windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
windows.geometry("600x700")
windows.resizable(0, 0)

# Cargar imagen de fondo
ruta_imagen = r"D:\PROYECTO_CON_TKINTER\Images\logo.png"
if os.path.exists(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 700))
    imagen_fondo = ImageTk.PhotoImage(imagen)
    label_fondo = tk.Label(windows, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
else:
    # Si no se encuentra la imagen, se crea una imagen en gris
    from PIL import ImageDraw
    imagen = Image.new("RGB", (600, 700), color="gray")
    draw = ImageDraw.Draw(imagen)
    draw.text((200,350), "Logo no encontrado", fill="white")
    imagen_fondo = ImageTk.PhotoImage(imagen)
    label_fondo = tk.Label(windows, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

frame_login = tk.Frame(windows, bg="#053A20", bd=2, relief="ridge")
frame_login.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

fuente_titulos = ("Century Gothic", 16, "bold")
fuente_texto = ("Century Gothic", 14, "bold")

tk.Label(frame_login, text="Bienvenido a System_GYM", font=fuente_titulos,
         fg="white", bg="#053A20").pack(pady=10)

tk.Label(frame_login, text="Usuario:", font=fuente_texto, fg="white", bg="#053A20").pack(pady=2)
entrada_usuario = tk.Entry(frame_login, font=("Century Gothic", 12))
entrada_usuario.pack(pady=2)

tk.Label(frame_login, text="Contraseña:", font=fuente_texto, fg="white", bg="#053A20").pack(pady=2)
entrada_contraseña = tk.Entry(frame_login, font=("Century Gothic", 12), show="*")
entrada_contraseña.pack(pady=2)

tk.Button(frame_login, text="Iniciar sesión", font=fuente_texto, bg="#28A745", fg="white",
          command=validar_login).pack(pady=20)

windows.mainloop()
