import time
import random
from collections import deque

class SistemaColas:
    def __init__(self, capacidad):
        self.cola = deque(maxlen=capacidad)
        self.capacidad = capacidad
        self.clientes_atendidos = 0
        self.clientes_rechazados = 0
        self.simulacion_activa = True

    def llegada_clientes(self):
        while self.simulacion_activa:

            nuevos_clientes = random.randint(0, 3)
            
            for _ in range(nuevos_clientes):
                cliente_id = f"C-{time.time():.0f}"
                if len(self.cola) < self.capacidad:
                    self.cola.append(cliente_id)
                    print(f"🟢 [Llegada] Cliente {cliente_id} | En cola: {len(self.cola)}/{self.capacidad}")
                else:
                    self.clientes_rechazados += 1
                    print(f"🔴 [Rechazado] Cola llena - Cliente {cliente_id}")
            
   
            time.sleep(random.uniform(1, 3))

    def atender_clientes(self):
        while self.simulacion_activa or self.cola:
            if self.cola:
                cliente = self.cola.popleft()
                print(f"🟡 [Atendiendo] Cliente {cliente} | Tiempo: 3 segundos...")
                time.sleep(3)
                self.clientes_atendidos += 1
                print(f"🟣 [Atendido] Cliente {cliente} | Total: {self.clientes_atendidos}")
            else:
                print("⚪ [Espera] No hay clientes en cola")
                time.sleep(1)

    def simular(self, duracion_total=30):
        print(f"\n=== INICIANDO SIMULACIÓN ===")
        print(f"Capacidad de cola: {self.capacidad}")
        print(f"Duración: {duracion_total} segundos\n")
        

        import threading
        hilo_llegadas = threading.Thread(target=self.llegada_clientes)
        hilo_llegadas.start()
        
    
        tiempo_inicio = time.time()
        while (time.time() - tiempo_inicio) < duracion_total:
            self.atender_clientes()
        

        self.simulacion_activa = False
        hilo_llegadas.join()
        
        print("\n=== ESTADÍSTICAS FINALES ===")
        print(f"Clientes atendidos: {self.clientes_atendidos}")
        print(f"Clientes rechazados: {self.clientes_rechazados}")
        print(f"Clientes en cola al finalizar: {len(self.cola)}")


if __name__ == "__main__":
    sistema = SistemaColas(capacidad=5)
    sistema.simular(duracion_total=10)