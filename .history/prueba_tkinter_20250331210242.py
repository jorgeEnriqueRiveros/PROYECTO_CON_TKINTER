import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


# ---- Función para abrir la ventana de consultas ----
def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Panel de Consultas")
    nueva_ventana.geometry("600x700")
    nueva_ventana.resizable(0, 0)

    # Imagen de fondo
    imagen_fondo_consulta = ImageTk.PhotoImage(imagen)
    label_fondo_consulta = tk.Label(nueva_ventana, image=imagen_fondo_consulta)
    label_fondo_consulta.place(x=0, y=0, relwidth=1, relheight=1)
    nueva_ventana.imagen_fondo_consulta = imagen_fondo_consulta  

    # Frame con transparencia simulada
    frame_consultas = tk.Frame(nueva_ventana, bg="#053A20", bd=2, relief="ridge")
    frame_consultas.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

    etiqueta_bienvenida = tk.Label(frame_consultas, text="Menú de Consultas", font=("Century Gothic", 16, "bold"), fg="white", bg="#053A20")
    etiqueta_bienvenida.pack(pady=10)

    # Función para mostrar mensaje en los botones
    def mostrar_mensaje(opcion):
        messagebox.showinfo("Información", f"Seleccionaste: {opcion}")

    # Lista de botones con texto y función asociada
    botones = [
        "Registrar Persona",
        "Registrar Producto",
        "Comprar",
        "Ver Información Cliente",
        "Ver Compras Cliente",
        "Sumar Valor Compras",
        "Ordenar Más Vendidos",
        "Salir"
    ]

    # Crear los botones dinámicamente con negrita y color verde oscuro
    for texto in botones:
        boton = tk.Button(frame_consultas, text=texto, font=("Century Gothic", 12, "bold"), bg="#157347", fg="white",
                          command=lambda t=texto: nueva_ventana.destroy() if t == "Salir" else mostrar_mensaje(t))
        boton.pack(pady=5, fill="x")

# ---- Función de validación de usuario ----
def validar_login():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    if usuario == "root" and contraseña == "123456":
        windows.withdraw()  # Oculta la ventana principal
        abrir_nueva_ventana()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ---- Crear ventana principal ----
windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
windows.geometry("600x700")
windows.resizable(0, 0)

# ---- Cargar imagen de fondo ----
ruta_imagen = r"D:\PROYECTO_CON_TKINTER\Images\logo.png"
if os.path.exists(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 700))
    imagen_fondo = ImageTk.PhotoImage(imagen)

    label_fondo = tk.Label(windows, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# ---- Simulación de Transparencia ----
frame_transparente = tk.Frame(windows, bg="#053A20", bd=2, relief="ridge")
frame_transparente.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

fuente_titulos = ("Century Gothic", 16, "bold")
fuente_texto = ("Century Gothic", 14, "bold")

# ---- Elementos dentro del frame ----
tk.Label(frame_transparente, text="Bienvenido a System_GYM", font=fuente_titulos, fg="white", bg="#053A20").pack(pady=10)

tk.Label(frame_transparente, text="Usuario:", font=fuente_texto, fg="white", bg="#053A20").pack()
entrada_usuario = tk.Entry(frame_transparente, font=("Century Gothic", 12))
entrada_usuario.pack(pady=5)

tk.Label(frame_transparente, text="Contraseña:", font=fuente_texto, fg="white", bg="#053A20").pack()
entrada_contraseña = tk.Entry(frame_transparente, font=("Century Gothic", 12), show="*")
entrada_contraseña.pack(pady=5)

tk.Button(frame_transparente, text="Iniciar sesión", font=fuente_texto, bg="#28A745", fg="white",
          command=validar_login).pack(pady=20)

# Mantener la ventana abierta
windows.mainloop()
