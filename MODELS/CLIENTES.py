class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.clientes = []#Lista vacia que almacena los datos de los clientes


def agregar_cliente(self, cliente):
    clientes.append(cliente)

def listar_clientes(self):
    return clientes

#Usa una expresión generadora (c for c in clientes) que recorre la lista y compara la cédula.
# next() retorna el primer cliente que coincide. Si no encuentra ninguno, devuelve None.
def buscar_cliente(self, cedula):
    return next((c for c in clientes if c.cedula == cedula), None)

def eliminar_cliente(self, cedula):
    global clientes #Usamos global porque vamos a modificar la lista global (no solo leerla).
    clientes = [c for c in clientes if c.cedula != cedula] #Esto crea una nueva lista excluyendo al cliente cuya cédula sea igual a la que pasamos.
