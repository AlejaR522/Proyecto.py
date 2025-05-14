class Cliente:
    clientes_registrados = []  # Lista estática para simular "base de datos"

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefo = telefono

    def guardar(self):
        Cliente.clientes_registrados.append(self)

    @staticmethod
    def obtener_todos():
        return Cliente.clientes_registrados

    @staticmethod
    def eliminar(id):
        Cliente.clientes_registrados = [c for c in Cliente.clientes_registrados if c.id != id]