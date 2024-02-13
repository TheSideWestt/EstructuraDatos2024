import os
import time
os.system('cls' if os.name == 'nt' else 'cls')

fila = []
#fila en Python

#Añadir elementos a la fila

fila.append('cliente1SC')
fila.append('cliente2NS')
fila.append('cliente3S')
print("Los elementos de la fila son:", fila)

#Atender cliente (eliminar elemento de la fila)

cliente_atendido = fila.pop(2)
print("\nEl primer cliente atendido fue: \n", cliente_atendido)
print("\nFila despues de atender: \n", fila)
time.sleep(2)

cliente_atendido = fila.pop(1)
print("\nEl segundo cliente atendido fue: \n", cliente_atendido)
print("\nFila despues de atender: \n", fila)
time.sleep(2)

cliente_atendido = fila.pop(0)
print("\nEl tercer cliente atendido fue: \n", cliente_atendido)
print("\nFila despues de atender, todos los clientes se han atendido \n",)
