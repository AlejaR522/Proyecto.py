# interfaces/productos_gui.py
from logging import root
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class VentanaProductos:
    def __init__(self, root,ventana_principal):
        self.root = root
        self.ventana_principal = ventana_principal

        self.root.title("Gestión de Productos")
        self.root.geometry("600x500")

        self.nombre_var = StringVar()
        self.precio_var = StringVar()
        self.stock_var = StringVar()

        Label(root, text="Gestión de Productos", font=("Times New Roman", 16)).pack(pady=10)

        Label(root, text="Nombre del Producto").pack()
        Entry(root, textvariable=self.nombre_var).pack()

        Label(root, text="Precio").pack()
        Entry(root, textvariable=self.precio_var).pack()

        Label(root, text="Stock").pack()
        Entry(root, textvariable=self.stock_var).pack()


        Frame_botones = Frame(root)
        Frame_botones.pack(pady=10)

        Button(Frame_botones, text="Guardar", command=self.guardar_producto).grid(row=0, column=0, padx=5)
        Button(Frame_botones, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=1, padx=5)
        Button(Frame_botones, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=5)
        btn_volver = ttk.Button(self.root, text="Volver", command=self.volver)
        btn_volver.pack(pady=20)
        
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Stock", text="Stock")

        self.tabla.column("ID", width=150)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Precio", width=80)
        self.tabla.column("Stock", width=100)

        self.tabla.pack(pady=20)

        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        self.mostrar_productos()

    def conectar(self):
        return sqlite3.connect("tienda.db")

    def guardar_producto(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                        (self.nombre_var.get(), self.precio_var.get(), self.stock_var.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Guardado", "Producto guardado correctamente")
        self.limpiar_campos()
        self.mostrar_productos()

    def volver(self):
        self.root.destroy()      # Cierra Ventana B
        self.ventana_principal.deiconify() # Muestra nuevamente Ventana A

    def mostrar_productos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        for fila in cursor.fetchall():
            self.tabla.insert("", END, values=fila)
        conn.close()

    def seleccionar_fila(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            self.id_seleccionado = valores[0]
            self.nombre_var.set(valores[1])
            self.precio_var.set(valores[2])
            self.stock_var.set(valores[3])

    def actualizar_producto(self):
        if not hasattr(self, 'id_seleccionado'):
            messagebox.showerror("Error", "Selecciona un producto para actualizar")
            return
    
        # Validación de campos
        try:
            precio = float(self.precio_var.get())
            stock = int(self.stock_var.get())
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número y Stock un entero")
            return
    
        conn = self.conectar()
        cursor = conn.cursor()
        try:
                cursor.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                        (self.nombre_var.get(), precio, stock, self.id_seleccionado))
                conn.commit()
                messagebox.showinfo("Actualizado", "Producto actualizado correctamente")
                self.mostrar_productos()
                self.limpiar_campos()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {str(e)}")
        finally:
            conn.close()


    def eliminar_producto(self): 
        try:
            conn = self.conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id_producto=?", (self.id_seleccionado,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Eliminado", "Producto eliminado correctamente")
            self.limpiar_campos()
            self.mostrar_productos()
        except AttributeError:
            messagebox.showerror("Error", "Selecciona un producto para eliminar")

    def limpiar_campos(self):
        self.nombre_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")
