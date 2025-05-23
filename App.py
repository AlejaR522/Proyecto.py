#Raquel Eunice Martines daza-
#Alejandra Tibidor-

import tkinter as tk
from GUI.Gui_Clientes import VentanaClientes
from GUI.main import VentanaPrincipal
from Databases import connect     # Inicializa la BD
from MODELS.CLIENTES import Cliente

def run_app():
    connect()  # Crea tablas si no existen
    root = tk.Tk()
    VentanaPrincipal(root)  # Llama a tu menú original
    root.mainloop()

def abrir_clientes(self):
    self.root.withdraw()  # Oculta ventana principal
    ventana_clientes = tk.Toplevel(self.root)
    VentanaClientes(ventana_clientes, self.root)  # Pasa referencia
    if not Cliente.obtener_todos():
        cliente1 = Cliente(1, "Juan Pérez", "Calle 123", "3001234567")
        cliente2 = Cliente(2, "María Gómez", "Avenida 456", "3109876543")
        cliente1.guardar()
        cliente2.guardar()

if __name__ == "__main__":
    run_app()  # Ejecuta todo desde aquí