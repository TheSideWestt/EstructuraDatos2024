import os
import time

# Limpieza de pantalla
os.system('clear' if os.name == 'nt' else 'clear')

class ColaPrioridad:
    def __init__(self):
        self.elementos = []
        self.contador = {}

    def encolar(self, item, prioridad):
        self.elementos.append((item, prioridad))
        self.elementos.sort(key=lambda x: x[1])  # Ordena por prioridad
        if item in self.contador:
            self.contador[item] += 1
        else:
            self.contador[item] = 1


    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)[0]
        else:
            raise IndexError("Desencolar de una cola vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

cola_prioridad = ColaPrioridad()
cola_prioridad.encolar('Cliente#1 Sin Cuenta', 3)  # Se agrega 'clienteSC' con prioridad 3
cola_prioridad.encolar('Cliente#2 No Suscrito', 2)  # Se agrega 'clienteNS' con prioridad 2
cola_prioridad.encolar('Cliente#3 Suscrito', 1)  # Se agrega 'clienteS' con prioridad 1
cola_prioridad.encolar('Cliente#4 Sin Cuenta', 3)
cola_prioridad.encolar('Cliente#5 No Susrito', 2)
cola_prioridad.encolar('Cliente#6 Suscrito', 1)

print("Elemento desencolado: \n", cola_prioridad.desencolar())
time.sleep(2)
print("\nElemento desencolado: \n", cola_prioridad.desencolar())
time.sleep(2)
print("\nElemento desencolado: \n", cola_prioridad.desencolar())
time.sleep(2)
print("\nElemento desencolado: \n", cola_prioridad.desencolar())
time.sleep(2)
print("\nElemento desencolado: \n", cola_prioridad.desencolar())
time.sleep(2)
print("\nElemento desencolado: \n", cola_prioridad.desencolar())
time.sleep(2)


print("\nTodos los elementos han sido desencolados",)  # Imprime el siguiente elemento desencolado (el de siguiente mayor prioridad)

while not cola_prioridad.esta_vacia():
    print("Elemento desencolado:", cola_prioridad.desencolar())
    time.sleep(2)  # Duerme 2 segundos
