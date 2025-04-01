import tkinter as tk

#en la variable ventana se almacena un objeto widget ventana creada con el metodo Tk

windows = tk.Tk()
windows.title("Mi primer proyecto con tkinter")
etiqueta1 = tk.Label(windows, text="Bienvenido al System_gym_db")
etiqueta1.pack() #metodo que organiza los widgets en la ventana
etiqueta2 = tk.Label(windows, text="Por favor ingrese su usuario y contraseña")
etiqueta2.pack()
windows.geometry("600x800")
windows.resizable("
windows.mainloop() #metodo que mantiene la ventana abierta

