import tkinter as tk
from tkinter import Toplevel, ttk
from GUI.Gui_Productos import VentanaProductos
from GUI.Gui_Clientes import VentanaClientes
from GUI.Gui_Facturas import VentanaFactura

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Tienda")
        self.root.geometry("600x400")

        # Título
        titulo = tk.Label(root, text="Gestión de Tienda", font=("Times new Roman", 25, "bold"), fg="saddle brown")
        titulo.pack(pady=35)

        # Frame para los botones
        marco_botones = tk.Frame(root)
        marco_botones.pack(pady=20)



        # Botones de navegación
        btn_productos = tk.Button(marco_botones, text="Gestionar Productos",font=("Times new Roman",16),width=18,bg="NavajoWhite3",fg="white", command=self.abrir_productos)
        btn_productos.grid(row=0, column=0, pady=5)

        btn_clientes = tk.Button(marco_botones, text="Gestionar Clientes",font=("Times new Roman",16),width=18,bg="NavajoWhite3",fg="white", command=self.abrir_clientes)
        btn_clientes.grid(row=1, column=0, pady=5)

        btn_facturas = tk.Button(marco_botones, text="Gestionar Facturas", font=("Times new Roman",16),width=18,bg="NavajoWhite3",fg="white", command=self.abrir_facturas)
        btn_facturas.grid(row=2, column=0, pady=5)

        # Botón salir
        btn_salir = tk.Button(root, text="Salir",font=("Times new Roman",13),width=5, command=root.quit, bg="red4", fg="White")
        btn_salir.pack(pady=10)

    def abrir_productos(self):
        self.root.withdraw()
        nueva_ventana = Toplevel(self.root)           # Nueva ventana secundaria
        VentanaProductos(nueva_ventana, self.root)  # Pasa self.root como ventana_principal
    

    def abrir_clientes(self):
        self.root.withdraw()
        nueva_ventana = Toplevel(self.root)           # Nueva ventana secundaria
        VentanaClientes(nueva_ventana, self.root)               # Llama la clase que define la interfaz de 

    def abrir_facturas(self):
        self.root.withdraw()  # Oculta ventana principal
        nueva_ventana = Toplevel(self.root)           # Nueva ventana secundaria
        VentanaFactura(nueva_ventana, self.root)               # Llama la clase que define la interfaz de 

