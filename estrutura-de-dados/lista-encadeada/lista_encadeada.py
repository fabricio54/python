from email.errors import StartBoundaryNotFoundDefect


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkdlist:
    def __init__(self):
        self.head = None
        self.tam = 0 

    def append(self, data):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = Node(data)

        else:
            self.head = Node(data)
        self.tam += 1

    def imprimir(self):
        if self.head:
            aux = self.head
            while aux:
                print(aux.data)
                aux = aux.next
                
        else:
            print('lista vazia!!!')

    def remove(self):
        if self.head:
            aux = self.head
            while aux.next:
                aux = aux.next
            del aux.data
            del aux
        else:
            print('lista vazia!!!')
    
    def remove(self, data):
        if self.head:
            aux = self.head
            while aux.next and aux.data != data:
                aux = aux.next
            if aux.data == data:
                del aux.data
                del aux
            else:
                print('Elemento não encontrado na lista!!!')
        else:
            print('lista vazia!!!')

    # 1. faça uma função para concatenar duas listas encadeadas
    def concatena(self, lista):
        if self.head:
            aux = self.head
            aux2 = lista.head
            while aux.next:
                aux = aux.next
            aux.next = aux2
            del lista.head
            del lista
            lista = Linkdlist()
            return lista
        else:
            print('Não tem elemento na lista!!!')
    
    # 2. Faça uma função que receba uma lista encadeada e a divida
    # em duas listas, cada uma com metade dos elementos.
    # Caso haja uma quantidade ímpar de elementos, a
    # primeira lista retornada deve conter um elemento a mais.


    def divide_lista(self, lista, lista2):
        if self.head:
            if self.tam % 2 == 0:
                aux = self.head
                cont = 0
                while aux:
                    if cont < (self.tam / 2):
                        lista.append(aux.data)
                    else:
                        lista2.append(aux.data)
                    aux = aux.next
                    cont += 1
            else:
                aux = self.head
                cont = 0
                while aux:
                    if cont < (self.tam // 2) + 1:
                        lista.append(aux.data)
                    else:
                        lista2.append(aux.data)
                    aux = aux.next
                    cont += 1
            del self.head
            self.head = None
    
    # 03. Dadas duas listas, verifique se ambas possume o mesmo tamanho. Em caso positivo, gere uma terceira lista contendo os elementos das duas listas recebidas intercalados.
    
    def intercalada(self, lista):
        if self.tam == lista.tam:
            lista_inter = Linkdlist()
            aux = self.head
            aux2 = lista.head
            while aux:
                lista_inter.append(aux.data)
                aux = aux.next
            while aux2:
                lista_inter.append(aux2.data)
                aux2 = aux2.next
            return lista_inter

        else:
            lista_inter = Linkdlist()
            return lista_inter
    
    # 04. faça uma função que receba uma lista e um valor. Retorne a primeira em que este valor aparece na lista.

    def retorno_pos(self, ele):
        if self.head:
            cont = 0
            aux = self.head
            while aux:
                if aux.data == ele:
                    return cont
                aux = aux.next
                cont += 1
            return None 
        return None
    
    # 05. Considere uma lista encadeada cujos elementos estão dispostos em ordem crescente. Faça uma função que receba esta lista e um valor a ser buscado. Informe a posição em que o valor apareceu. Para tanto, execute busca binária.
     
    def __getitem__(self, index):
        aux = self.head
        for i in range(index):
            if aux:
                aux = aux.next
            else:
                raise IndexError("list index out of range")
        if aux:
            return aux.data
        else:
            raise IndexError("list index out of range")
        
    def get(self, index):
        return self.__getitem__(index)
    
    def __setitem__(self, index, elem):
        aux = self.head
        for i in range(index):
            if aux:
                aux = aux.next
            else:
                raise IndexError("list index out of range")
        if aux:
            aux.data = elem
        else:
            raise IndexError("list index out of range")
    
    def set(self, index, elem):
        self.__setitem__(index, elem)

    def busca_valor(self, value):
        for i in range(self.tam):
            if self[i] == value:
                return i
        return None


    def eh_crescente(self):
        for i in range(self.tam):
            for j in range(self.tam):
                if self[i] > self[j]:
                    return False
        return True

    def ordenar(self):
        aux = None
        for i in range(self.tam):
            for j in range(self.tam):
                if self[i] < self[j]:
                    aux = self[j]
                    self[j] = self[i]
                    self[i] = aux

    def busca_ordem_crescente(self, value):
        if self.head:
            if not self.eh_crescente():
                self.ordenar()
            return self.busca_valor(value)
        else:
            raise IndexError("list index out of range")

    # 06. refaça a questão 5 com a busca binária.

    def busca_binaria(self, index, inicio, fim):
        meio = (inicio + fim) // 2
        if index < self[meio]:
            self.busca_binaria(index, inicio, meio+1)
        elif index > self[meio]:
            self.busca_binaria(index, meio, fim)
        return meio

    def busca_bin(self, index):
        if self.head:
            if not self.eh_crescente():
                return self.busca_binaria(index, 0, (self.tam)-1)
            


lista = Linkdlist()
lista.append(3)
lista.append(1)
lista.append(2)
lista.append(6)
lista.append(4)

print(lista.busca_bin(3))
#print(lista.busca_ordem_crescente(2))