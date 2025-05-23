# PRODUCTOS.py
from Databases import get_db_connection

class Producto:
    def __init__(self, nombre, precio, stock, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def guardar(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:  # Nuevo producto
            cursor.execute(
                "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                (self.nombre, self.precio, self.stock)
            )
            self.id = cursor.lastrowid
        else:  # Actualizar existente
            cursor.execute(
                "UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                (self.nombre, self.precio, self.stock, self.id)
            )
        conn.commit()
        conn.close()

    @staticmethod 
    def obtener_todos():
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos")
            productos = [Producto(id=row[0], nombre=row[1], precio=row[2], stock=row[3]) for row in cursor.fetchall()]
            conn.close()
            return productos
    
    @staticmethod
    def obtener_por_nombre(nombre):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        row = cursor.fetchone()
        conn.close()
        if row:
                return Producto(id=row[0], nombre=row[1], precio=row[2], stock=row[3])
        return None