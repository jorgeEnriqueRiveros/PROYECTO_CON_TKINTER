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

# Función para cargar la imagen de fondo (si no se encuentra, se genera una imagen gris)
def cargar_imagen_fondo(ancho, alto):
    if os.path.exists(RUTA_IMAGEN):
        imagen = Image.open(RUTA_IMAGEN)
        imagen = imagen.resize((ancho, alto))
    else:
        imagen = Image.new("RGB", (ancho, alto), color="gray")
        draw = ImageDraw.Draw(imagen)
        draw.text((ancho//2 - 50, alto//2), "Logo no encontrado", fill="white")
    return ImageTk.PhotoImage(imagen)

# Función personalizada para mostrar mensajes de guardado/información con estilo consistente
def mostrar_mensaje_custom(titulo, mensaje):
    mensaje_win = tk.Toplevel()
    mensaje_win.title(titulo)
    mensaje_win.geometry("300x150")
    mensaje_win.resizable(False, False)
    mensaje_win.configure(bg="#053A20")
    
    # Centrar la ventana en la pantalla
    mensaje_win.update_idletasks()
    x = (mensaje_win.winfo_screenwidth() - 300) // 2
    y = (mensaje_win.winfo_screenheight() - 150) // 2
    mensaje_win.geometry(f"+{x}+{y}")
    
    label = tk.Label(mensaje_win, text=mensaje, font=("Century Gothic", 12, "bold"),
                     fg="white", bg="#053A20")
    label.pack(expand=True)
    
    tk.Button(mensaje_win, text="Aceptar", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=mensaje_win.destroy).pack(pady=10)

# Función auxiliar para crear ventanas de consulta con formato consistente
def crear_ventana_consulta(titulo="Consulta", ancho=600, alto=700):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    ventana.resizable(0, 0)
    imagen_fondo = cargar_imagen_fondo(ancho, alto)
    label_fondo = tk.Label(ventana, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.imagen_fondo = imagen_fondo
    # Frame central con el mismo formato en todas las ventanas
    frame = tk.Frame(ventana, bg="#053A20", bd=2, relief="ridge")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=int(ancho*0.65), height=int(alto*0.65))
    return ventana, frame

# ===============================================================
# Funciones GUI para cada acción
# ===============================================================

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
    
    # Lista para almacenar los productos agregados al carrito
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
        # Se obtiene el id del cliente a partir del correo
        id_cliente = Cliente.obtener_id_cliente(correo)
        if not id_cliente:
            messagebox.showerror("Error", "Cliente no encontrado")
            return
        
        # Se crea una instancia de Compra y se agregan los productos del carrito
        compra = Compra(id_cliente, forma_pago)
        for prod in productos:
            compra.agregar_producto(*prod)
        
        try:
            # Se guarda la compra (esto inserta en la tabla de compras y en la de detalles)
            compra.guardar_compra()
            # Se muestra un mensaje de éxito y se cierra la ventana actual
            mostrar_mensaje_custom("Éxito", "Compra registrada correctamente", ventana.destroy)
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar la compra:\n{e}")
    
    tk.Button(frame, text="Finalizar Compra", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=finalizar_compra).pack(pady=10)
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

# Función para cerrar sesión: cierra el panel de consultas y vuelve a mostrar el login
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
    
    # Crear botones para diferentes acciones
    frame_panel = tk.Frame(panel, bg="#053A20", bd=2, relief="ridge")
    frame_panel.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)
    
    tk.Button(frame_panel, text="Registrar Cliente", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=registrar_cliente_gui).pack(pady=10)
    tk.Button(frame_panel, text="Registrar Producto", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=registrar_producto_gui).pack(pady=10)
    tk.Button(frame_panel, text="Realizar Compra", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=realizar_compra_gui).pack(pady=10)
    tk.Button(frame_panel, text="Cerrar Sesión", font=("Century Gothic", 12, "bold"),
              bg="#157347", fg="white", command=lambda: cerrar_sesion(panel)).pack(pady=10)

# Ventana de login
windows = tk.Tk()
windows.title("Login")
windows.geometry("400x300")
windows.resizable(0, 0)

tk.Label(windows, text="Usuario", font=("Century Gothic", 12, "bold")).pack(pady=5)
entrada_usuario = tk.Entry(windows, font=("Century Gothic", 12))
entrada_usuario.pack(pady=5)

tk.Label(windows, text="Contraseña", font=("Century Gothic", 12, "bold")).pack(pady=5)
entrada_contraseña = tk.Entry(windows, font=("Century Gothic", 12), show="*")
entrada_contraseña.pack(pady=5)

tk.Button(windows, text="Ingresar", font=("Century Gothic", 12, "bold"),
          bg="#157347", fg="white", command=validar_login).pack(pady=20)

windows.mainloop()
