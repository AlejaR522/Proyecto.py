# interfaces/clientes_gui.py

from tkinter import *
from tkinter import messagebox, ttk

class VentanaClientes:
    def __init__(self, root, ventana_cli):
        self.root = root
        self.ventana_cli = ventana_cli

        self.root.title("Gestión de Clientes")
        self.root.geometry("600x500")

        # Lista en memoria para clientes
        self.clientes = []

        # Variables
        self.id = StringVar()
        self.nombre_var = StringVar()
        self.telefono_var = StringVar()

        # Título
        Label(root, text="Gestión de Clientes", font=("Times new Roman", 16)).pack(pady=15)

        # Entradas
        Label(root, text="Nombre Completo").pack()
        Entry(root, textvariable=self.nombre_var).pack()

        Label(root, text="ID:"). pack()
        Entry (root, textvariable=self.id).pack()


        Label(root, text="Teléfono").pack()
        Entry(root, textvariable=self.telefono_var).pack()

        # Botones
        Frame_botones = Frame(root)
        Frame_botones.pack(pady=15)

        Button(Frame_botones, text="Guardar", command=self.guardar_cliente,bg="NavajoWhite3",fg="white").grid(row=0, column=0, padx=5)
        Button(Frame_botones, text="Actualizar", command=self.actualizar_cliente,bg="NavajoWhite3",fg="white").grid(row=0, column=1, padx=5)
        Button(Frame_botones, text="Eliminar", command=self.eliminar_cliente,bg="red4",fg="white").grid(row=0, column=2, padx=5)
        btn_volver = ttk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.pack(pady=20)


        # Tabla de clientes
        self.tabla = ttk.Treeview(root, columns=("ID","Nombre", "Teléfono"), show='headings')
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Teléfono", text="Teléfono")

        self.tabla.column("ID", width=60)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Teléfono", width=120)

        self.tabla.pack(pady=20)

        # Evento de selección en la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)


    def guardar_cliente(self):
        id = self.id.get()
        nombre = self.nombre_var.get()
        telefono = self.telefono_var.get()

        if nombre == "" or id == "" or telefono == "":
            messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
            return

        # Guardar en memoria
        self.clientes.append((id, nombre, telefono))
        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Guardar", "Cliente guardado exitosamente.")

    def actualizar_cliente(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccionar", "Seleccione un cliente de la tabla.")
            return

        idx = self.tabla.index(seleccion[0])
        self.clientes[idx] = (
            self.nombre_var.get(),
            self.id.get(),
            self.telefono_var.get()
        )
        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Actualizar", "Cliente actualizado.")

    def eliminar_cliente(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccionar", "Seleccione un cliente para eliminar.")
            return

        idx = self.tabla.index(seleccion[0])
        del self.clientes[idx]
        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Eliminar", "Cliente eliminado.")

    def actualizar_tabla(self):
        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Insertar clientes
        for cliente in self.clientes:
            self.tabla.insert('', END, values=cliente)

    def volver(self):
        self.root.destroy()      # Cierra Ventana B
        self.ventana_cli.deiconify() # Muestra nuevamente Ventana A

    def seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion[0])
            valores = item['values']
            self.nombre_var.set(valores[0])
            self.direccion_var.set(valores[1])
            self.telefono_var.set(valores[2])

    # Añade este método para obtener la lista de clientes
    def obtener_clientes(self):
        return self.clientes  # Retorna la lista de clientes [(id, nombre, teléfono), ...]

    def limpiar_campos(self):
        self.nombre_var.set("")
        self.id.set("")
        self.telefono_var.set("")
