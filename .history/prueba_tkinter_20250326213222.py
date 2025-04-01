import tkinter as tk
from PIL import Image, ImageTk
import os

# Crear ventana
windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
windows.geometry("600x700")
windows.resizable(0, 0)

# Verificar si la imagen existe
ruta_imagen = r"D:\PROYECTO_CON_TKINTER\Images\logo.png"
if not os.path.exists(ruta_imagen):
    print("⚠️ ERROR: La imagen no existe en la ruta especificada")
    windows.destroy()  # Cierra la ventana si la imagen no se encuentra

# Cargar imagen de fondo
try:
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 700))
    imagen_fondo = ImageTk.PhotoImage(imagen)
except Exception as e:
    print(f"⚠️ ERROR al cargar la imagen: {e}")
    windows.destroy()

# Agregar imagen de fondo con Label
label_fondo = tk.Label(windows, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Frame con fondo oscuro (sin transparencia real)
frame = tk.Frame(windows, bg="#053A20", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

# Etiqueta "Bienvenido"
etiqueta1 = tk.Label(frame, text="Bienvenido al System_gym_db", font=("Arial", 16, "bold"), fg="white", bg="#053A20")
etiqueta1.pack(pady=10)

# Mensaje adicional
mensaje = tk.Label(frame, text="Ingresa tu usuario y contraseña", font=("Arial", 12, "bold"), fg="white", bg="#053A20")
mensaje.pack(pady=5)

# Etiqueta "Usuario"
etiqueta_usuario = tk.Label(frame, text="Usuario:", font=("Arial", 14, "bold"), fg="white", bg="#053A20")
etiqueta_usuario.pack()

# Campo de entrada para usuario
entrada_usuario = tk.Entry(frame, font=("Arial", 14), width=25)
entrada_usuario.pack(pady=5)

# Etiqueta "Contraseña"
etiqueta_contraseña = tk.Label(frame, text="Contraseña:", font=("Arial", 14, "bold"), fg="white", bg="#053A20")
etiqueta_contraseña.pack()

# Campo de entrada para contraseña
entrada_contraseña = tk.Entry(frame, font=("Arial", 14), show="*", width=25)
entrada_contraseña.pack(pady=5)

# Botón de inicio de sesión
boton_login = tk.Button(frame, text="Iniciar sesión", font=("Arial", 14, "bold"), bg="#28A745", fg="white", width=15)
boton_login.pack(pady=15)

# Ejecutar ventana
windows.mainloop()
