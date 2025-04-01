import tkinter as tk
from PIL import Image, ImageTk
import os

# Crear ventana
windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
windows.geometry("600x800")
windows.resizable(0, 0)

# Obtener la ruta de la imagen en la misma carpeta del script
ruta_imagen = r"D:\PROYECTO_CON_TKINTER\Images\logo.png"

# Cargar imagen de fondo
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((600, 800))  # Ajustar al tamaño de la ventana
imagen_fondo = ImageTk.PhotoImage(imagen)

# Agregar imagen de fondo con Label
label_fondo = tk.Label(windows, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Marco para centrar los elementos
frame = tk.Frame(windows, bg="#053A20")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta "Bienvenido"
etiqueta1 = tk.Label(frame, text="Bienvenido al System_gym_db", font=("Arial", 14), fg="white", bg="#053A20")
etiqueta1.pack(pady=10)

# Mensaje adicional
mensaje = tk.Label(frame, text="Ingresa tu usuario y contraseña para iniciar sesión", font=("Arial", 10), fg="white", bg="#053A20")
mensaje.pack(pady=5)

# Etiqueta "Ingrese usuario"
etiqueta_usuario = tk.Label(frame, text="Usuario:", font=("Arial", 12), fg="white", bg="#053A20")
etiqueta_usuario.pack()

# Campo de entrada para usuario
entrada_usuario = tk.Entry(frame, font=("Arial", 12), width=25)
entrada_usuario.pack(pady=5)

# Etiqueta "Ingrese contraseña"
etiqueta_contraseña = tk.Label(frame, text="Contraseña:", font=("Arial", 12), fg="white", bg="#053A20")
etiqueta_contraseña.pack()

# Campo de entrada para contraseña
entrada_contraseña = tk.Entry(frame, font=("Arial", 12), show="*", width=25)  # show="*" oculta la contraseña
entrada_contraseña.pack(pady=5)

# Botón de inicio de sesión
boton_login = tk.Button(frame, text="Iniciar sesión", font=("Arial", 12), bg="#28A745", fg="white")
boton_login.pack(pady=10)

# Ejecutar ventana
windows.mainloop()
