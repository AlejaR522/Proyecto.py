# Database.py
import sqlite3

class Producto:
    def __init__(self, nombre, precio, stock, id_producto=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @staticmethod
    def conectar():
        return sqlite3.connect("tienda.db")

    @staticmethod
    def crear_tabla():
        conexion = Producto.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        conexion.commit()
        conexion.close()

    def guardar(self):
        conexion = Producto.conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                       (self.nombre, self.precio, self.stock))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_todos():
        conexion = Producto.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos

    @staticmethod
    def actualizar(id_producto, nombre, precio, stock):
        conexion = Producto.conectar()
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, precio = ?, stock = ?
            WHERE id_producto = ?
        ''', (nombre, precio, stock, id_producto))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_producto):
        conexion = Producto.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
        conexion.commit()
        conexion.close()
        
