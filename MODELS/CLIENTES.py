class Cliente:
    # Lista estática que mantendrá todos los clientes en memoria
    _clientes = []  # Usamos _ para indicar que es "privado"
    
    def __init__(self, id, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def guardar(self):
        """Guarda el cliente en la lista en memoria"""
        if not any(c.id == self.id for c in Cliente._clientes):
            Cliente._clientes.append(self)
    
    @classmethod
    def obtener_todos(cls):
        """Devuelve todos los clientes"""
        return cls._clientes
    
    @classmethod
    def obtener_por_id(cls, id):
        """Busca un cliente por su ID"""
        for cliente in cls._clientes:
            if cliente.id == id:
                return cliente
        return None
    
    @classmethod
    def eliminar(cls, id):
        """Elimina un cliente por su ID"""
        cls._clientes = [c for c in cls._clientes if c.id != id]