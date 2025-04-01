import tkinter as tk
from PIL import Image, ImageTk
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
    imagen = imagen.resize((600, 700))  # Ajustar al tamaño de la ventana
    imagen_fondo = ImageTk.PhotoImage(imagen)

    # Agregar imagen de fondo
    label_fondo = tk.Label(windows, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Cargar imagen semi-transparente para el Frame
ruta_frame = r"D:\PROYECTO_CON_TKINTER\Images\frame_transparente.png"
if os.path.exists(ruta_frame):
    img_frame = Image.open(ruta_frame)
    img_frame = img_frame.resize((350, 300))
    img_frame = ImageTk.PhotoImage(img_frame)

    # Agregar imagen de fondo del Frame
    label_frame_bg = tk.Label(windows, image=img_frame, bg="#053A20")
    label_frame_bg.place(relx=0.5, rely=0.5, anchor="center")

# Crear Frame sobre la imagen de fondo
frame = tk.Frame(windows, bg="#053A20", bd=5)  # Simula transparencia
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

# Etiqueta "Bienvenido"
etiqueta1 = tk.Label(frame, text="Bienvenido al System_gym_db", font=("Arial", 16, "bold"), fg="white", bg="#053A20")
etiqueta1.pack(pady=10)

# Etiqueta "Ingrese usuario"
etiqueta_usuario = tk.Label(frame, text="Usuario:", font=("Arial", 14, "bold"), fg="white", bg="#053A20")
etiqueta_usuario.pack()

# Campo de entrada para usuario
entrada_usuario = tk.Entry(frame, font=("Arial", 12))
entrada_usuario.pack(pady=5)

# Etiqueta "Ingrese contraseña"
etiqueta_contraseña = tk.Label(frame, text="Contraseña:", font=("Arial", 14, "bold"), fg="white", bg="#053A20")
etiqueta_contraseña.pack()

# Campo de entrada para contraseña
entrada_contraseña = tk.Entry(frame, font=("Arial", 12), show="*")
entrada_contraseña.pack(pady=5)

# Botón de inicio de sesión
boton_login = tk.Button(frame, text="Iniciar sesión", font=("Arial", 14, "bold"), bg="#28A745", fg="white")
boton_login.pack(pady=20)

# Mantener la ventana abierta
windows.mainloop()
