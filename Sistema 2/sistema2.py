from collections import deque

cola=deque()


def agregar_cliente(cliente):
    if len(cola) >= capacidad:
        print("No se pudo agregar el cliente "+cliente)
        return False
    cola.append(cliente)
    print("cliente "+ cliente +" agregado")
    return True
def atender_cliente():
    if not cola:
        print("no hay clientes para atender")
        return None
    siguiente=cola.popleft()
    print("Atendiendo a "+siguiente)
    return siguiente
def siguiente_cliente():
    if not cola:
        print("No hay nadie esperando")
        return None
    print("Siguiente para atender"+ cola[0])
    return cola[0]


capacidad=2 # Capacidad de n personas
print("Clientes en espera:")
print(cola)
agregar_cliente("Ana")
agregar_cliente("Marcos")
agregar_cliente("Pedro")
atender_cliente()
print("Clientes en espera:")
print(cola)
atender_cliente()
atender_cliente()
print("Clientes en espera:")
print(cola)