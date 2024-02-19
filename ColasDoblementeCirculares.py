import os
os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        if data % 2 != 0:  # Solo agrega números impares a la cola
            new_node = Node(data)
            if self.is_empty():
                new_node.next = new_node
                self.head = new_node
            else:
                new_node.next = self.head.next
                self.head.next = new_node
                self.head = new_node
            print("\nSe agregó el número", data, "a la cola")

    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía")
            return None
        data = self.head.next.data
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.next = self.head.next.next
        print("Se eliminó el número", data, "de la cola")
        return data

    def display(self):
        if self.is_empty():
            print("La cola está vacía")
            return
        current = self.head.next
        while current != self.head:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data)


# Ejemplo de uso
queue = CircularQueue()

# Inserción y visualización
queue.enqueue(1)
queue.display()
queue.enqueue(3)
queue.display()
queue.enqueue(5)
queue.display()
queue.enqueue(7)
queue.display()
queue.enqueue(9)
queue.display()

# Eliminación y visualización
print("\nEliminado:", queue.dequeue())
queue.display()
print("\# NOTE: Eliminado:", queue.dequeue())
queue.display()
print("\nEliminado:", queue.dequeue())
queue.display()
print("\nEliminado:", queue.dequeue())
queue.display()
print("\nEliminado:", queue.dequeue())
queue.display()
