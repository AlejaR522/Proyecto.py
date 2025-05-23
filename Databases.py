# Databases.py
import sqlite3

def get_db_connection():
    """Crea y devuelve una conexión a la base de datos"""
    return sqlite3.connect('Tienda.db')

def connect():
    """Crea la tabla de productos si no existe"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Resto de funciones (sin cambios)
def insertar_producto(nombre, precio, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                    (nombre, precio, stock))
    conn.commit()
    producto_id = cursor.lastrowid
    conn.close()
    return producto_id

def obtener_productos():
    """Devuelve una lista de tuplas con los productos"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY nombre")
    productos = cursor.fetchall()
    conn.close()
    return productos

def obtener_producto_por_nombre(nombre):
    """Obtiene un producto por su nombre (para facturación)"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def obtener_producto_por_id(id):
    """Obtiene un producto por su ID"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def actualizar_producto(id, nombre, precio, stock):
    """Actualiza un producto existente"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos 
        SET nombre = ?, precio = ?, stock = ?
        WHERE id = ?
    """, (nombre, precio, stock, id))
    conn.commit()
    conn.close()

def actualizar_stock_producto(id, nuevo_stock):
    """Actualiza solo el stock de un producto"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, id))
    conn.commit()
    conn.close()

def eliminar_producto(id):
    """Elimina un producto de la BD"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def buscar_productos(termino):
    """Busca productos por término (nombre)"""
    conn = sqlite3.connect("Tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f'%{termino}%',))
    productos = cursor.fetchall()
    conn.close()
    return productos