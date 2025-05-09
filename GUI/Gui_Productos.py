# interfaz.py

import tkinter as tk
from tkinter import ttk
from MODELS.PRODUCTOS import Producto  # importa tu modelo

# Crea productos de prueba
productos = [
    Producto("Camisa", 50000, 20),
    Producto("Pantalón", 75000, 15),
    Producto("Zapatos", 120000, 10)
]

# Función para mostrar productos en el widget Text
def mostrar_productos():
    texto.delete("1.0", tk.END)  # Limpia el Text antes de mostrar
    for p in productos:
        texto.insert(tk.END, p.mostrar())

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Inventario de Productos")
ventana.geometry("400x300")

# Botón para mostrar productos
btn_mostrar = ttk.Button(ventana, text="Mostrar Productos", command=mostrar_productos)
btn_mostrar.pack(pady=10)

# Área de texto para mostrar los productos
texto = tk.Text(ventana, height=15, width=45)
texto.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
