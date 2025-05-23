from tkinter import *
from tkinter import messagebox, ttk
from Databases import obtener_producto_por_nombre, actualizar_stock_producto
from MODELS.CLIENTES import Cliente
from MODELS.FACTURAS import Factura
from MODELS.PRODUCTOS import Producto

class VentanaFactura:
    def __init__(self, root, ventana_fact):
        self.root = root
        self.ventana_fact = ventana_fact
        self.items_factura = []  # Para almacenar productos temporales
        
        self.root.title("Factura")
        self.root.geometry("800x600")

        # Frame principal
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        Label(main_frame, text="Generar Factura", font=("Times New Roman", 16)).grid(row=0, column=0, columnspan=3, pady=15)

        # Cliente
        Label(main_frame, text="Cliente:").grid(row=1, column=0, sticky=W)
        self.cliente_cb = ttk.Combobox(main_frame, state="readonly")
        self.cliente_cb.grid(row=1, column=1, sticky=EW, padx=5, pady=5)
        self.actualizar_clientes()

        # Producto
        Label(main_frame, text="Producto:").grid(row=2, column=0, sticky=W)
        self.producto_cb = ttk.Combobox(main_frame)
        self.producto_cb.grid(row=2, column=1, sticky=EW, padx=5, pady=5)
        self.actualizar_productos()

        # Cantidad
        Label(main_frame, text="Cantidad:").grid(row=3, column=0, sticky=W)
        self.cantidad_var = StringVar()
        Entry(main_frame, textvariable=self.cantidad_var).grid(row=3, column=1, sticky=EW, padx=5, pady=5)

        # Botones
        btn_frame = Frame(main_frame)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=10)

        Button(btn_frame, text="Agregar Producto", command=self.agregar_producto, bg="blue", fg="white").pack(side=LEFT, padx=5)
        Button(btn_frame, text="Generar Factura", command=self.generar_factura, bg="green4", fg="white").pack(side=LEFT, padx=5)
        Button(btn_frame, text="Nueva Factura", command=self.limpiar_factura, bg="orange", fg="white").pack(side=LEFT, padx=5)
        Button(btn_frame, text="Volver", command=self.volver).pack(side=LEFT, padx=5)

        # Tabla para mostrar items de la factura
        self.tabla = ttk.Treeview(main_frame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings")
        self.tabla.heading("Producto", text="Producto")
        self.tabla.heading("Precio", text="Precio Unitario")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Subtotal", text="Subtotal")

        for col in ("Producto", "Precio", "Cantidad", "Subtotal"):
            self.tabla.column(col, width=120, anchor=CENTER)

        self.tabla.grid(row=5, column=0, columnspan=3, pady=20, sticky=NSEW)

        # Total
        self.total_var = StringVar()
        self.total_var.set("Total: $0")
        Label(main_frame, textvariable=self.total_var, font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=3)

        # Configurar expansión
        main_frame.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

    def actualizar_clientes(self):
        clientes = Cliente.obtener_todos()
        self.cliente_cb['values'] = [f"{c.nombre} (ID: {c.id})" for c in clientes]

    def actualizar_productos(self):
        productos = Producto.obtener_todos()
        self.producto_cb['values'] = [p.nombre for p in productos]  # Accede al atributo nombre

    def agregar_producto(self):
        producto_nombre = self.producto_cb.get()
        cantidad = self.cantidad_var.get()

        if not producto_nombre or not cantidad:
            messagebox.showerror("Error", "Debe seleccionar un producto y cantidad")
            return

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número positivo")
            return

        producto = obtener_producto_por_nombre(producto_nombre)
        if not producto:
            messagebox.showerror("Error", "Producto no encontrado")
            return

        precio = float(producto[2])
        stock = int(producto[3])

        if cantidad > stock:
            messagebox.showerror("Error", f"Stock insuficiente. Disponible: {stock}")
            return

        subtotal = precio * cantidad
        self.items_factura.append((producto, cantidad))

        # Actualizar tabla
        self.tabla.insert('', 'end', values=(producto_nombre, f"${precio:,.2f}", cantidad, f"${subtotal:,.2f}"))

        # Actualizar total
        total = sum(float(item[0][2]) * item[1] for item in self.items_factura)
        self.total_var.set(f"Total: ${total:,.2f}")

        # Limpiar campos
        self.cantidad_var.set("")
        self.producto_cb.set("")

    def generar_factura(self):
        if not self.items_factura:
            messagebox.showerror("Error", "Debe agregar al menos un producto")
            return

        cliente_idx = self.cliente_cb.current()
        if cliente_idx == -1:
            messagebox.showerror("Error", "Debe seleccionar un cliente")
            return

        cliente = Cliente.obtener_todos()[cliente_idx]
        
        # Crear factura
        factura = Factura(cliente, self.items_factura)
        factura_id = factura.guardar()

        # Actualizar stocks
        for producto, cantidad in self.items_factura:
            actualizar_stock_producto(producto[1], int(producto[3]) - cantidad)

        messagebox.showinfo("Éxito", f"Factura #{factura_id} generada\nTotal: ${factura.total:,.2f}")
        self.limpiar_factura()

    def limpiar_factura(self):
        self.items_factura = []
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        self.total_var.set("Total: $0")
        self.cantidad_var.set("")
        self.producto_cb.set("")

    def volver(self):
        self.root.destroy()
        self.ventana_fact.deiconify()