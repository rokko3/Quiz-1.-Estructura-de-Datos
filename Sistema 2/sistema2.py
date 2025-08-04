import time
from collections import deque
import random

class SistemaAtencionClientes:
    def __init__(self, capacidad_maxima):
        self.cola_clientes = deque()
        self.capacidad_maxima = capacidad_maxima

    def cliente_llega(self):
        # LLegada aleatoria de un cliente 50%
        return random.choice([True, False])

    def atender_cliente(self):
        if self.cola_clientes:
            cliente = self.cola_clientes.popleft()
            print(f"Atendiendo al cliente: {cliente}")
            time.sleep(0.5)  # tiempo de atencion
            print(f"Cliente {cliente} finalizado.")
            return True
        return False

    def espacio_disponible(self):
        return len(self.cola_clientes) < self.capacidad_maxima

    def agregar_cliente(self, cliente_id):
        if self.espacio_disponible():
            self.cola_clientes.append(cliente_id)
            print(f"Cliente {cliente_id} agregado a la cola.")
        else:
            print(f"Cola llena. Cliente {cliente_id} espera espacio...")

            # Esperar a que se libere un espacio
            while not self.espacio_disponible():
                time.sleep(0.5)
                self.atender_cliente()  # Simula que se atiende alguien y se libera espacio

            self.cola_clientes.append(cliente_id)
            print("Cliente "+cliente_id +"agregado a la cola tras liberar espacio.")

    def ejecutar(self, total_clientes):
        cliente_id = 1
        while cliente_id <= total_clientes:
            print("\nEsperando cliente nuevo...")
            time.sleep(0.5)
            if self.cliente_llega():
                print(f"Cliente {cliente_id} ha llegado.")
                self.agregar_cliente(cliente_id)
                self.atender_cliente()
                cliente_id += 1
            else:
                print("No llegó ningún cliente en este ciclo.")
                time.sleep(0.5)

# Simulación del sistema
sistema = SistemaAtencionClientes(capacidad_maxima=3)
sistema.ejecutar(total_clientes=10)
