from Databases import obtener_producto_por_nombre, actualizar_stock_producto

# En Models.py (clase Factura)
class Factura:
    facturas = []  # Lista en memoria

    def __init__(self, cliente, items):  # items = [(producto, cantidad), ...]
        self.cliente = cliente
        self.items = items
        # producto[0] = id, producto[2] = precio, producto[3] = stock
        self.total = sum(producto[2] * cantidad for producto, cantidad in items)

    def guardar(self):
        # 1. Actualizar el stock de cada producto en la BD
        for producto, cantidad in self.items:
            nuevo_stock = producto[3] - cantidad  # Stock actual - cantidad vendida
            actualizar_stock_producto(producto[0], nuevo_stock)  # producto[0] = ID
            
        # 2. Guardar la factura en la lista (memoria)
        Factura.facturas.append(self)