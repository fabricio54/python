class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkdlist:
    def __init__(self, data=None):
        self.head = Node(data)

    def append(self, data):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Node(data)
        else:
            self.head = Node(data)

    def imprimir(self):
        if self.head:
            aux = self.head
            while aux:
                print(aux.data)
                aux = aux.next
    
    def pop(self):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            del aux.data
            aux = None 
        else:
            return None
    

list = Linkdlist(3)
list.append(4)
list.append(1)
list.append(5)
list.append(7)

list.imprimir()
list.pop()
print()
list.imprimir()