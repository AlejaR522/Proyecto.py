class Factura:
    facturas = []  # Lista en memoria

    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente  # Objeto Cliente
        self.producto = producto  # Lista de objetos Producto
        self.cantidad = cantidad
        self.total = sum(p.precio for p in producto)

    def guardar(self):
        Factura.facturas.append(self)

    @staticmethod
    def obtener_por_cliente(id_cliente):
        return [f for f in Factura.facturas if f.cliente.id == id_cliente]