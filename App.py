#Raquel Eunice Martines daza-
#Alejandra Tibidor-

import tkinter as tk
from GUI.Gui_Clientes import VentanaClientes
from GUI.main import VentanaPrincipal
from Databases import connect     # Inicializa la BD

def run_app():
    connect()  # Crea tablas si no existen
    root = tk.Tk()
    VentanaPrincipal(root)  # Llama a tu menú original
    root.mainloop()

def abrir_clientes(self):
    self.root.withdraw()  # Oculta ventana principal
    ventana_clientes = tk.Toplevel(self.root)
    VentanaClientes(ventana_clientes, self.root)  # Pasa referencia
if __name__ == "__main__":
    run_app()  # Ejecuta todo desde aquí