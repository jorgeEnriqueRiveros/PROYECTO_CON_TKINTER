import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import os

# Crear ventana
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

    # Agregar imagen de fondo
    label_fondo = tk.Label(windows, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# ---- Simulación de Transparencia en el Formulario ----

# Crear un Frame semi-transparente
frame_transparente = tk.Canvas(windows, bg="#053A20", highlightthickness=0)
frame_transparente.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

# Reducir opacidad del fondo del frame usando un color RGBA (esto no funciona en todos los sistemas)
windows.tk_setPalette(background="#053A2080")  # 80 es el nivel de transparencia (00-FF)

# Etiqueta "Bienvenido"
etiqueta1 = tk.Label(frame_transparente, text="Bienvenido al System_gym_db", font=("Arial", 16, "bold"), fg="white", bg="#053A20")
etiqueta1.pack(pady=10)

# Etiqueta "Ingrese usuario"
etiqueta_usuario = tk.Label(frame_transparente, text="Usuario:", font=("Arial", 14, "bold"), fg="white", bg="#053A20")
etiqueta_usuario.pack()

# Campo de entrada para usuario
entrada_usuario = tk.Entry(frame_transparente, font=("Arial", 12))
entrada_usuario.pack(pady=5)

# Etiqueta "Ingrese contraseña"
etiqueta_contraseña = tk.Label(frame_transparente, text="Contraseña:", font=("Arial", 14, "bold"), fg="white", bg="#053A20")
etiqueta_contraseña.pack()

# Campo de entrada para contraseña
entrada_contraseña = tk.Entry(frame_transparente, font=("Arial", 12), show="*")
entrada_contraseña.pack(pady=5)

# Botón de inicio de sesión
boton_login = tk.Button(frame_transparente, text="Iniciar sesión", font=("Arial", 14, "bold"), bg="#28A745", fg="white")
boton_login.pack(pady=20)

# Mantener la ventana abierta
windows.mainloop()
