import tkinter as tk

#en la variable ventana se almacena un objeto widget ventana creada con el metodo Tk

windows = tk.Tk()
windows.title("Programa SYSTEM_GYM")
etiqueta1 = tk.Label(windows, text="Bienvenido al System_gym_db")
etiqueta1.pack() #metodo que organiza los widgets en la ventana
etiqueta2 = tk.Label(windows, text="Por favor ingrese su usuario y contraseña")
etiqueta2.pack()
windows.geometry("600x800")
windows.resizable(0,0)
windows.configure(bg="#053A20", width=600, height=800)
windows.mainloop() #metodo que mantiene la ventana abierta

