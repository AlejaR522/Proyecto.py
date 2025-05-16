from tkinter import *
from tkinter import messagebox, ttk
from Databases import obtener_producto_por_nombre, actualizar_stock_producto

class VentanaFactura:
    def __init__(self, root, ventana_fact):
        self.root = root
        self.ventana_fact = ventana_fact
    
        self.root.title("Factura")
        self.root.geometry("600x500")

        Label(root, text="Generar Factura", font=("Times New Roman", 16)).pack(pady=10)

        self.cliente_var = StringVar()
        self.producto_var = StringVar()
        self.cantidad_var = StringVar()

        Label(root, text="Nombre del Cliente").pack()
        Entry(root, textvariable=self.cliente_var).pack()

        Label(root, text="Producto").pack()
        Entry(root, textvariable=self.producto_var).pack()

        Label(root, text="Cantidad").pack()
        Entry(root, textvariable=self.cantidad_var).pack()

        Button(root, text="Generar Factura", command=self.generar_factura).pack(pady=15)
        btn_volver = ttk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.pack(pady=20)

        # Tabla para mostrar factura
        self.tabla = ttk.Treeview(root, columns=("Cliente", "Producto", "Cantidad", "Total"), show="headings")
        self.tabla.heading("Cliente", text="Cliente")
        self.tabla.heading("Producto", text="Producto")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Total", text="Total")

        self.tabla.column("Cliente", width=150)
        self.tabla.column("Producto", width=150)
        self.tabla.column("Cantidad", width=80)
        self.tabla.column("Total", width=100)

        self.tabla.pack(pady=20)

    def volver(self):
        self.root.destroy()      # Cierra Ventana B
        self.ventana_fact.deiconify() # Muestra nuevamente Ventana A

    def generar_factura(self):
        cliente = self.cliente_var.get()
        producto_nombre = self.producto_var.get()
        cantidad = self.cantidad_var.get()

        if not cliente or not producto_nombre or not cantidad:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            cantidad = int(cantidad)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número")
            return

        producto = obtener_producto_por_nombre(producto_nombre)

        if not producto:
            messagebox.showerror("Error", "Producto no encontrado")
            return

        precio = float(producto[2])  # producto[2] = precio
        stock = int(producto[3])     # producto[3] = inventario

        if cantidad > stock:
            messagebox.showerror("Error", f"Stock insuficiente. Disponible: {stock}")
            return

        total = cantidad * precio

        # Mostrar en la tabla
        self.tabla.insert('', 'end', values=(cliente, producto_nombre, cantidad, f"${total:,.0f}"))

        # Actualizar stock en base de datos
        actualizar_stock_producto(producto_nombre, stock - cantidad)

        messagebox.showinfo("Factura", f"Factura generada exitosamente\nTotal a pagar: ${total:,.0f}")
