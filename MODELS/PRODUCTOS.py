import sqlite3
from Databases import get_db_connection  # Asumo que tienes esta función en Databases.py

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def guardar(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (self.nombre, self.precio, self.stock)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()
        return productos

    # Más métodos (actualizar, eliminar, buscar por nombre)...