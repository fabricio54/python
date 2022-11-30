
class Tree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def append(self, data):
        if not self.data:
            self.data = data
        elif data < self.data:
            if self.left:
                self.left.append(data)
            else:
                self.left = Tree(data)
        elif data > self.data:
            if self.right:
                self.right.append(data)
            else:
                self.right = Tree(data)

                
    def imprime_pre_ordem(self):
        if self.data:
            if self.left:
                self.left.imprime_pre_ordem()
            print(self.data)
            if self.right:
                self.right.imprime_pre_ordem()

    def imprime_ordem(self):
        if self.data:
            print(self.data)
            if self.left:
                self.left.imprime_ordem()
            if self.right:
                self.right.imprime_ordem()

    def imprime_pos_ordem(self):
        if self.data:
            if self.left:
                self.left.imprime_pos_ordem()
            if self.right:
                self.right.imprime_pos_ordem()
            print(self.data)
    
    def sheets_node(self):
        esq = 0 
        dir = 0
        if self.data is None:
            return 0
        elif self.data and not self.left and not self.right:
            return 1
        else:
            if self.left:
                dir = self.left.sheets_node()
            if self.right:
                esq = self.right.sheets_node()
            return esq + dir
    
    def grade(self):
        e = d = 0
        if not self.data:
            return 0
        elif not self.left and not self.right:
            return 1
        else:
            if self.left:
                e = self.left.grade() + 1
                if self.right:
                    e -= 1
            if self.right:
                d = self.right.grade() + 1
                if self.left:
                    d -= 1
        return e + d
    
    # verificar se um certo valor n está presente na árvore.
    def verifica_valor(self, valor):
        if not self.data:
            return False
        elif self.data == valor:
            return True
        elif valor < self.data and self.left:
            return self.left.verifica_valor(valor)
        elif valor > self.data and self.right:
            return self.right.verifica_valor(valor)
        return False

    # retornar o maior valor presente na arvore
    def retorna_maior_valor(self):
        if not self.data:
            return None
        elif self.data and not self.right:
            return self.data
        else:
            return self.right.retorna_maior_valor()
    
    # retornar o menor valor presente na arvore
    def retorna_menor_valor(self):
        if not self.data:
            return None
        elif self.data and not self.left:
            return self.data
        else:
            return self.left.retorna_menor_valor()
    
    # quantidade de elementos
    def quantidade_elemento(self):
        e = d = 0
        if not self.data:
            return -1
        if not self.left and not self.right:
            return 0
        else:
            if self.left:
                e = self.left.quantidade_elemento() + 1
            if self.right:
                d = self.right.quantidade_elemento() + 1
        return e + d
        
    
    # retornar a média dos valores presentes em uma árvore.
    def soma(self):
        quant = 0
        if not self.data:
            return 0
        if self.data:
            quant += self.data
        if self.left:
            quant += self.left.soma()
        if self.right:
            quant += self.right.soma()
        return quant

    def media(self):
        return self.soma() / (self.quantidade_elemento() + 1)

        
        



arvore = Tree()
arvore.append(5)
arvore.append(9)
arvore.append(2)
arvore.append(3)
arvore.append(21)
arvore.append(14)
#print("Pré-Ordem")
#arvore.imprime_pre_ordem()
#print("Ordem")
#arvore.imprime_ordem()
#print("Pos-Ordem")
#arvore.imprime_pos_ordem()
#print(arvore.grade())
#print(arvore.verifica_valor(4))
#print(arvore.retorna_maior_valor())
#print(arvore.retorna_menor_valor())
print(arvore.media())





                 

    