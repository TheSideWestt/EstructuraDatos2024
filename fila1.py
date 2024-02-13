import os
os.system('cls' if os.name == 'nt' else 'clear')

fila = []
#fila en Python

#Añadir elementos a la fila

fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
print("Los elementos de la fila son:", fila)

#Atender cliente (eliminar elemento de la fila)

cliente_atendido = fila.pop(0)
print("El primer cliente atendido fue:", cliente_atendido)
print("Fila despues de atender:", fila)
