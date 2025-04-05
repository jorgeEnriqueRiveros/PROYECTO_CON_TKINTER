import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import os

# Importa las clases y funciones definidas en Sistema_Gym.py y Pool_Conexion.py
from Sistema_Gym import Cliente, Producto, Compra
from Pool_Conexion import Conexion

# Ruta de la imagen de fondo (se utiliza en todas las ventanas)
RUTA_IMAGEN = r"D:\PROYECTO_CON_TKINTER\Images\logo.png"

# ===============================================================
# Funciones de Utilidad
# ===============================================================

def cargar_imagen_fondo(ancho, alto):
    if os.path.exists(RUTA_IMAGEN):
        imagen = Image.open(RUTA_IMAGEN)
        imagen = imagen.resize((ancho, alto))
    else:
        imagen = Image.new("RGB", (ancho, alto), color="gray")
        draw = ImageDraw.Draw(imagen)
        draw.text((ancho//2 - 50, alto//2), "Logo no encontrado", fill="white")
    return ImageTk.PhotoImage(imagen)

def mostrar_mensaje_custom(titulo, mensaje, callback=None):
    mensaje_win = tk.Toplevel()
    mensaje_win.title(titulo)
    mensaje_win.geometry("300x150")
    mensaje_win.resizable(False, False)
    mensaje_win.configure(bg="#053A20")
    
    mensaje_win.update_idletasks()
    x = (mensaje_win.winfo_screenwidth() - 300) // 2
    y = (mensaje_win.winfo_screenheight() - 150) // 2
    mensaje_win.geometry(f"+{x}+{y}")
    
    label = tk.Label(mensaje_win, text=mensaje, font=("Century Gothic", 12, "bold"),
                     fg="white", bg="#053A20")
    label.pack(expand=True)
    
    tk.Button(mensaje_win, text="Aceptar", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", 
              command=lambda: [mensaje_win.destroy(), callback() if callback else None]
             ).pack(pady=10)

def crear_ventana_consulta(titulo="Consulta", ancho=600, alto=700):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    ventana.resizable(0, 0)
    imagen_fondo = cargar_imagen_fondo(ancho, alto)
    label_fondo = tk.Label(ventana, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.imagen_fondo = imagen_fondo
    frame = tk.Frame(ventana, bg="#053A20", bd=2, relief="ridge")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=int(ancho*0.65), height=int(alto*0.65))
    return ventana, frame

# ===============================================================
# Funciones GUI para cada acción
# ===============================================================

def registrar_cliente_gui():
    ventana, frame = crear_ventana_consulta("Registrar Cliente", 600, 700)
    
    tk.Label(frame, text="Registrar Cliente", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    campos = ["Nombre:", "Apellido:", "Teléfono:", "Correo:", "Membresía:"]
    entries = {}
    for campo in campos:
        tk.Label(frame, text=campo, font=("Century Gothic", 12, "bold"),
                 fg="white", bg="#053A20").pack(pady=2)
        entrada = tk.Entry(frame, font=("Century Gothic", 12))
        entrada.pack(pady=2)
        entries[campo] = entrada

    def guardar_cliente():
        nombre = entries["Nombre:"].get()
        apellido = entries["Apellido:"].get()
        telefono = entries["Teléfono:"].get()
        correo = entries["Correo:"].get()
        membresia = entries["Membresía:"].get()
        if nombre and apellido and telefono and correo and membresia:
            cliente = Cliente(nombre, apellido, telefono, correo, membresia)
            try:
                cliente.guardar()
                mostrar_mensaje_custom("Éxito", "Cliente registrado correctamente", ventana.destroy)
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar cliente:\n{e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    tk.Button(frame, text="Guardar", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=guardar_cliente).pack(pady=10)
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

def registrar_producto_gui():
    ventana, frame = crear_ventana_consulta("Registrar Producto", 600, 700)
    
    tk.Label(frame, text="Registrar Producto", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    tk.Label(frame, text="Nombre del Producto:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_nombre = tk.Entry(frame, font=("Century Gothic", 12))
    entry_nombre.pack(pady=5)
    
    tk.Label(frame, text="Precio Unitario:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_precio = tk.Entry(frame, font=("Century Gothic", 12))
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
                mostrar_mensaje_custom("Éxito", "Producto registrado correctamente", ventana.destroy)
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar producto:\n{e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    tk.Button(frame, text="Guardar", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=guardar_producto).pack(pady=10)
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

def realizar_compra_gui():
    ventana, frame = crear_ventana_consulta("Realizar Compra", 600, 700)
    
    tk.Label(frame, text="Realizar Compra", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    tk.Label(frame, text="Correo del Cliente:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_correo = tk.Entry(frame, font=("Century Gothic", 12))
    entry_correo.pack(pady=5)
    
    tk.Label(frame, text="Forma de Pago:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_pago = tk.Entry(frame, font=("Century Gothic", 12))
    entry_pago.pack(pady=5)
    
    # Lista para almacenar productos agregados
    productos = []
    
    frame_producto = tk.Frame(frame, bg="#053A20")
    frame_producto.pack(pady=10)
    
    tk.Label(frame_producto, text="ID Producto:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").grid(row=0, column=0, padx=5, pady=2)
    entry_id_producto = tk.Entry(frame_producto, font=("Century Gothic", 12))
    entry_id_producto.grid(row=0, column=1, padx=5, pady=2)
    
    tk.Label(frame_producto, text="Cantidad:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").grid(row=1, column=0, padx=5, pady=2)
    entry_cantidad = tk.Entry(frame_producto, font=("Century Gothic", 12))
    entry_cantidad.grid(row=1, column=1, padx=5, pady=2)
    
    tk.Label(frame_producto, text="Precio Unitario:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").grid(row=2, column=0, padx=5, pady=2)
    entry_precio = tk.Entry(frame_producto, font=("Century Gothic", 12))
    entry_precio.grid(row=2, column=1, padx=5, pady=2)
    
    lista_productos = tk.Listbox(frame, font=("Century Gothic", 12))
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
        entry_id_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    
    tk.Button(frame_producto, text="Agregar Producto", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)
    
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
            mostrar_mensaje_custom("Éxito", "Compra registrada correctamente", ventana.destroy)
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar la compra:\n{e}")
    
    tk.Button(frame, text="Finalizar Compra", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=finalizar_compra).pack(pady=10)
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

def ver_info_cliente_gui():
    ventana, frame = crear_ventana_consulta("Ver Información del Cliente", 600, 700)
    
    tk.Label(frame, text="Ver Información del Cliente", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    tk.Label(frame, text="Correo del Cliente:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_correo = tk.Entry(frame, font=("Century Gothic", 12))
    entry_correo.pack(pady=5)
    
    info_text = tk.Text(frame, height=10, font=("Century Gothic", 12))
    info_text.pack(pady=10, fill="both", expand=True)
    
    def buscar_cliente():
        correo = entry_correo.get()
        cliente = Cliente.obtener_cliente_por_correo(correo)
        info_text.delete("1.0", tk.END)
        if cliente:
            info_text.insert(tk.END, str(cliente))
        else:
            messagebox.showerror("Error", "Cliente no encontrado")
    
    tk.Button(frame, text="Buscar", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=buscar_cliente).pack(pady=5)
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

def ver_compras_cliente_gui():
    ventana, frame = crear_ventana_consulta("Ver Compras del Cliente", 600, 700)
    
    tk.Label(frame, text="Ver Compras del Cliente", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    tk.Label(frame, text="Correo del Cliente:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_correo = tk.Entry(frame, font=("Century Gothic", 12))
    entry_correo.pack(pady=5)
    
    compras_text = tk.Text(frame, height=15, font=("Century Gothic", 12))
    compras_text.pack(pady=10, fill="both", expand=True)
    
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
    
    tk.Button(frame, text="Buscar Compras", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=buscar_compras).pack(pady=5)
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

def sumar_valor_compras_gui():
    ventana, frame = crear_ventana_consulta("Sumar Valor de Compras", 600, 700)
    
    tk.Label(frame, text="Sumar Valor de Compras", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    tk.Label(frame, text="Correo del Cliente:", font=("Century Gothic", 12, "bold"),
             fg="white", bg="#053A20").pack(pady=5)
    entry_correo = tk.Entry(frame, font=("Century Gothic", 12))
    entry_correo.pack(pady=5)
    
    resultado_label = tk.Label(frame, text="", font=("Century Gothic", 12, "bold"),
                               fg="white", bg="#053A20")
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
    
    tk.Button(frame, text="Sumar Compras", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=sumar_compras).pack(pady=5)
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

def ordenar_productos_gui():
    ventana, frame = crear_ventana_consulta("Productos Más Vendidos", 600, 700)
    
    tk.Label(frame, text="Productos Más Vendidos", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    productos_text = tk.Text(frame, height=20, font=("Century Gothic", 12))
    productos_text.pack(pady=10, fill="both", expand=True)
    
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
    
    tk.Button(frame, text="Volver al menú", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=ventana.destroy).pack(pady=5)

# ===============================================================
# Funciones de Login y Panel Principal
# ===============================================================

def validar_login():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    if usuario == "root" and contraseña == "123456":
        windows.withdraw()  # Oculta la ventana de login
        abrir_panel_consultas()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def cerrar_sesion(panel):
    panel.destroy()
    windows.deiconify()

def abrir_panel_consultas():
    panel = tk.Toplevel()
    panel.title("Panel de Consultas")
    panel.geometry("600x700")
    panel.resizable(0, 0)
    
    imagen_fondo_panel = cargar_imagen_fondo(600, 700)
    label_fondo_panel = tk.Label(panel, image=imagen_fondo_panel)
    label_fondo_panel.place(x=0, y=0, relwidth=1, relheight=1)
    panel.imagen_fondo_panel = imagen_fondo_panel
    
    frame_menu = tk.Frame(panel, bg="#053A20", bd=2, relief="ridge")
    frame_menu.place(relx=0.5, rely=0.5, anchor="center", width=400, height=600)
    
    tk.Label(frame_menu, text="Menú de Consultas", font=("Century Gothic", 16, "bold"),
             fg="white", bg="#053A20").pack(pady=10)
    
    botones = [
        ("Registrar Cliente", registrar_cliente_gui),
        ("Registrar Producto", registrar_producto_gui),
        ("Realizar Compra", realizar_compra_gui),
        ("Ver Información Cliente", ver_info_cliente_gui),
        ("Ver Compras Cliente", ver_compras_cliente_gui),
        ("Sumar Valor Compras", sumar_valor_compras_gui),
        ("Ordenar Productos Más Vendidos", ordenar_productos_gui)
    ]
    
    for texto, funcion in botones:
        tk.Button(frame_menu, text=texto, font=("Century Gothic", 12, "bold"),
                  bg="#157347", fg="white", command=funcion).pack(pady=5, fill="x")
    
    tk.Button(frame_menu, text="Salir", font=("Century Gothic", 12, "bold"),
              bg="#dc3545", fg="white", command=lambda: cerrar_sesion(panel)).pack(pady=10, fill="x")

# ===============================================================
# Ventana de Login Principal
# ===============================================================

windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
windows.geometry("600x700")
windows.resizable(0, 0)

imagen_fondo = cargar_imagen_fondo(600, 700)
label_fondo = tk.Label(windows, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

frame_login = tk.Frame(windows, bg="#053A20", bd=2, relief="ridge")
frame_login.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

tk.Label(frame_login, text="Bienvenido a System_GYM", font=("Century Gothic", 16, "bold"),
         fg="white", bg="#053A20").pack(pady=10)
tk.Label(frame_login, text="Usuario:", font=("Century Gothic", 14, "bold"),
         fg="white", bg="#053A20").pack(pady=2)
entrada_usuario = tk.Entry(frame_login, font=("Century Gothic", 12))
entrada_usuario.pack(pady=2)
tk.Label(frame_login, text="Contraseña:", font=("Century Gothic", 14, "bold"),
         fg="white", bg="#053A20").pack(pady=2)
entrada_contraseña = tk.Entry(frame_login, font=("Century Gothic", 12), show="*")
entrada_contraseña.pack(pady=2)
tk.Button(frame_login, text="Iniciar sesión", font=("Century Gothic", 14, "bold"),
          bg="#28A745", fg="white", command=validar_login).pack(pady=20)

windows.mainloop()
