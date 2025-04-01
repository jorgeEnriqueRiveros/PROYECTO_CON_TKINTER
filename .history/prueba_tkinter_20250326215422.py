import tkinter as tk
import 
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ---- Configuración de usuario y contraseña ----
USUARIO_CORRECTO = "root"
CONTRASEÑA_CORRECTA = "123456"

# ---- Función para validar usuario ----
def validar_credenciales():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    if usuario == USUARIO_CORRECTO and contraseña == CONTRASEÑA_CORRECTA:
        messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
        windows.withdraw()  # Oculta la ventana principal
        abrir_nueva_ventana()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ---- Función para abrir nueva ventana ----
def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Consulta de Base de Datos")
    nueva_ventana.geometry("600x700")
    nueva_ventana.resizable(0, 0)

    # Imagen de fondo en la nueva ventana
    imagen_fondo_consulta = ImageTk.PhotoImage(imagen)
    label_fondo_consulta = tk.Label(nueva_ventana, image=imagen_fondo_consulta)
    label_fondo_consulta.place(x=0, y=0, relwidth=1, relheight=1)
    nueva_ventana.imagen_fondo_consulta = imagen_fondo_consulta  # Evita que la imagen se elimine por el recolector de basura

    # Color de fondo para los widgets
    color_fondo = "#053A20"

    # Frame con transparencia simulada
    frame_consultas = tk.Frame(nueva_ventana, bg=color_fondo, bd=2, relief="ridge")
    frame_consultas.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

    etiqueta_bienvenida = tk.Label(frame_consultas, text="Panel de Consultas", 
                                   font=("Century Gothic", 16, "bold"), fg="white", bg=color_fondo)
    etiqueta_bienvenida.pack(pady=20)

    boton_salir = tk.Button(frame_consultas, text="Cerrar sesión", font=("Century Gothic", 12, "bold"),
                            bg="red", fg="white", command=lambda: [nueva_ventana.destroy(), windows.deiconify()])
    boton_salir.pack(pady=10)

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
color_fondo = "#053A20"

frame_transparente = tk.Frame(windows, bg=color_fondo, bd=2, relief="ridge")
frame_transparente.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

# ---- Fuente personalizada ----
fuente_titulos = ("Century Gothic", 16, "bold")
fuente_texto = ("Century Gothic", 14, "bold")

# ---- Elementos dentro del frame ----
etiqueta1 = tk.Label(frame_transparente, text="Bienvenido a System_GYM", font=fuente_titulos, fg="white", bg=color_fondo)
etiqueta1.pack(pady=10)

etiqueta_usuario = tk.Label(frame_transparente, text="Usuario:", font=fuente_texto, fg="white", bg=color_fondo)
etiqueta_usuario.pack()
entrada_usuario = tk.Entry(frame_transparente, font=("Century Gothic", 12))
entrada_usuario.pack(pady=5)

etiqueta_contraseña = tk.Label(frame_transparente, text="Contraseña:", font=fuente_texto, fg="white", bg=color_fondo)
etiqueta_contraseña.pack()
entrada_contraseña = tk.Entry(frame_transparente, font=("Century Gothic", 12), show="*")
entrada_contraseña.pack(pady=5)

# Botón de inicio de sesión con validación
boton_login = tk.Button(frame_transparente, text="Iniciar sesión", font=fuente_texto, bg="#28A745", fg="white",
                        relief="raised", bd=3, command=validar_credenciales)
boton_login.pack(pady=20)

# Mantener la ventana abierta
windows.mainloop()
