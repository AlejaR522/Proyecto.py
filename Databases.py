import sqlite3

# Conexión y creación de tabla
def connect():
    conn = sqlite3.connect('Tienda.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insertar producto
def insertar_producto(nombre, precio, stock):
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                    (nombre, precio, stock))
    conexion.commit()
    conexion.close()

# Obtener todos los productos
def obtener_productos():
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos

# Obtener producto por nombre (para factura)
def obtener_producto_por_nombre(nombre):
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

# Actualizar producto completo
def actualizar_producto(id, nombre, precio, stock):
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos
        SET nombre = ?, precio = ?, stock = ?
        WHERE id = ?
    """, (nombre, precio, stock, id))
    conexion.commit()
    conexion.close()

# Actualizar solo el stock de un producto (usado en factura)
def actualizar_stock_producto(id, nuevo_stock):
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, id))
    conexion.commit()
    conexion.close()

# Eliminar producto
def eliminar_producto(id):
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()

def limpiar_tabla():
    conexion = sqlite3.connect("Tienda.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos")
    conexion.commit()
    conexion.close()
# Llamada inicial para crear la tabla

