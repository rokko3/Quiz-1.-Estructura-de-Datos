import time # libreria para el tiempo
from collections import deque #agregar la cola
import random #para probabilidad de llegar cliente

class Sistema:
    def __init__(self, capacidad_maxima):
        self.cola_clientes = deque()
        self.capacidad_maxima = capacidad_maxima

    def cliente_llega(self):
        # LLegada aleatoria de un cliente 50%
        return random.choice([True, False])

    def atender_cliente(self):
        if self.cola_clientes: # verifica si hay clientes en la cola
            cliente = self.cola_clientes.popleft() #
            print("Atendiendo al cliente:" +cliente)
            time.sleep(0.5)  # tiempo de atencion
            print("Cliente"+ cliente+ "finalizado")
            return True
        return False

    def espacio_disponible(self):
        return len(self.cola_clientes) < self.capacidad_maxima #verifica si hay espacio disponible para agregar en la cola dependiendo del a capacidad maxima

    def agregar_cliente(self, cliente_id):
        if self.espacio_disponible():
            self.cola_clientes.append(cliente_id)
            print("Cliente" + cliente_id + "agregado a la cola")
        else:
            print("Cola llena, cliente"+ cliente_id+" en espera")

            # Esperar a que se libere un espacio
            while not self.espacio_disponible():
                time.sleep(0.5)
                self.atender_cliente()  # Simula que se atiende alguien y se libera espacio

            self.cola_clientes.append(cliente_id) # agrega el cliente
            print("Cliente "+cliente_id +"agregado a la cola tras liberar espacio.")

    def ejecutar(self, total_clientes):
        cliente_id = 1 #simula la entrada de clientes
        while cliente_id <= total_clientes: 
            print("\nEsperando cliente nuevo...")
            time.sleep(0.5)
            if self.cliente_llega():
                print("Cliente"+ cliente_id+ "ha llegado.")
                self.agregar_cliente(cliente_id)
                self.atender_cliente()
                cliente_id += 1
            else:
                print("No llego ningun cliente en este tiempo.")
                time.sleep(0.5)

sistema = Sistema(capacidad_maxima=3) # seleccionar la capacidad de atencion
sistema.ejecutar(total_clientes=10)
