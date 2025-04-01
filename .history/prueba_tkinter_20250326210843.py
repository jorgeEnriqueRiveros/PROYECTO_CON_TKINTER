import tkinter as tk
from PIL import Image, ImageTk  # Necesario para imágenes PNG y JPG

# Crear ventana
windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
windows.geometry("600x800")
windows.resizable(0, 0)

# Cargar imagen de fondo
imagen = Image.open("/Images")  # Asegúrate de que la imagen está en la misma carpeta
imagen = imagen.resize((600, 800))  # Ajustar al tamaño de la ventana
imagen_fondo = ImageTk.PhotoImage(imagen)

# Agregar imagen de fondo con Label
label_fondo = tk.Label(windows, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ajustar al tamaño de la ventana

# Agregar etiquetas de texto encima de la imagen
etiqueta1 = tk.Label(windows, text="Bienvenido al System_gym_db", font=("Arial", 14), fg="white", bg="#053A20")
etiqueta1.pack(pady=20)

etiqueta2 = tk.Label(windows, text="Por favor ingrese su usuario y contraseña", font=("Arial", 12), fg="white", bg="#053A20")
etiqueta2.pack(pady=10)

windows.mainloop()  # Mantener la ventana abierta
