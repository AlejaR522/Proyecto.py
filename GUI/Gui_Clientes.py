from tkinter import *
from tkinter import messagebox, ttk
from MODELS.CLIENTES import Cliente  # Importamos la clase Cliente del modelo

class VentanaClientes:
    def __init__(self, root, ventana_cli):
        self.root = root
        self.ventana_cli = ventana_cli

        self.root.title("Gestión de Clientes")
        self.root.geometry("600x500")

        # Variables
        self.id_var = StringVar()
        self.nombre_var = StringVar()
        self.telefono_var = StringVar()

        # Título
        Label(root, text="Gestión de Clientes", font=("Times new Roman", 16)).pack(pady=15)

        # Entradas
        Label(root, text="ID:").pack()
        Entry(root, textvariable=self.id_var).pack()

        Label(root, text="Nombre Completo").pack()
        Entry(root, textvariable=self.nombre_var).pack()

        Label(root, text="Teléfono").pack()
        Entry(root, textvariable=self.telefono_var).pack()

        # Botones
        Frame_botones = Frame(root)
        Frame_botones.pack(pady=15)

        Button(Frame_botones, text="Guardar", command=self.guardar_cliente, bg="NavajoWhite3", fg="white").grid(row=0, column=0, padx=5)
        Button(Frame_botones, text="Actualizar", command=self.actualizar_cliente, bg="NavajoWhite3", fg="white").grid(row=0, column=1, padx=5)
        Button(Frame_botones, text="Eliminar", command=self.eliminar_cliente, bg="red4", fg="white").grid(row=0, column=2, padx=5)
        btn_volver = ttk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.pack(pady=20)

        # Tabla de clientes
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Teléfono"), show='headings')
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Teléfono", text="Teléfono")

        self.tabla.column("ID", width=60)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Teléfono", width=120)

        self.tabla.pack(pady=20)

        # Evento de selección en la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        # Cargar clientes existentes
        self.actualizar_tabla()

    def guardar_cliente(self):
        id = self.id_var.get()
        nombre = self.nombre_var.get()
        telefono = self.telefono_var.get()

        if not id or not nombre or not telefono:
            messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
            return

        # Verificar si el ID ya existe
        if Cliente.obtener_por_id(id):
            messagebox.showwarning("Error", "Ya existe un cliente con este ID.")
            return

        # Crear y guardar el nuevo cliente
        nuevo_cliente = Cliente(id=id, nombre=nombre, direccion="", telefono=telefono)
        nuevo_cliente.guardar()

        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Guardar", "Cliente guardado exitosamente.")

    def actualizar_cliente(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccionar", "Seleccione un cliente de la tabla.")
            return

        id_actual = self.tabla.item(seleccion[0])['values'][0]
        cliente = Cliente.obtener_por_id(id_actual)
        
        if cliente:
            cliente.nombre = self.nombre_var.get()
            cliente.telefono = self.telefono_var.get()
            # Actualizamos el cliente en la lista
            Cliente.actualizar_cliente(cliente)
            
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Actualizar", "Cliente actualizado.")

    def eliminar_cliente(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccionar", "Seleccione un cliente para eliminar.")
            return

        id_cliente = self.tabla.item(seleccion[0])['values'][0]
        Cliente.eliminar(id_cliente)
        
        self.actualizar_tabla()
        self.limpiar_campos()
        messagebox.showinfo("Eliminar", "Cliente eliminado.")

    def actualizar_tabla(self):
        # Limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Insertar clientes desde la clase Cliente
        for cliente in Cliente.obtener_todos():
            self.tabla.insert('', END, values=(cliente.id, cliente.nombre, cliente.telefono))

    def volver(self):
        self.root.destroy()
        self.ventana_cli.deiconify()

    def seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion[0])
            valores = item['values']
            self.id_var.set(valores[0])
            self.nombre_var.set(valores[1])
            self.telefono_var.set(valores[2])

    def limpiar_campos(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.telefono_var.set("")