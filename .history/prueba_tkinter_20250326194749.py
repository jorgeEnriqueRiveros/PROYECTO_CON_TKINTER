import tkinter as tk

#en la variable ventana se almacena un objeto widget ventana creada con el metodo Tk

windows = tk.Tk()
windows.title("Mi primer proyecto con tkinter")
etiqueta1 = tk.Label(windows, text="Bienvenido a mi programa")

windows.mainloop() #metodo que mantiene la ventana abierta

