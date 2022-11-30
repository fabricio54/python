''' listas em python
Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5. este array será sempre do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.
Já em python:

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adiciondo elementos:
- Qualquer tipo de dado: Não possuem tipo de dado fixo: ou seja. podemos colocar qualquer tipo de vetor.
As listas em python são representações por colchetes : []'''

type([]) # criação de uma lista vazia

lista1 = [1, 55, 55, 6, 2, 6, 99, 23, 12, 9] # lista de números inteiros

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y'] # lista de strings

lista3 = [] # lista vazia

lista4 = list(range(11)) # lista com um range de 1 a 10

lista5 = list('Geek university') # a mesma lista de string, so que feita de outra forma

#  podemos rapidamente analizar a lista e verificar se o elemento existe dentro da lista
num = 55
if num in lista1:
    print(f'o número {num} existe na lista')
else:
    print(f'o número {num} não existe na lista')

#  podemos também ordenar uma lista atraves dos metodos
lista1.sort()
print(lista1)

#  podemos vericar também o número de ocorrências que ocorre dentro da lista
print(lista1.count(55))
print(lista2.count('e'))

#  adicionar elementos na lista com a função append
print(lista1)
lista1.append(5)
print(lista1)

#  adicionando uma lista dentro da lista
lista1.append([1, 3, 65])
print(lista1)
''' observação: Não podemos adicionar mais de um elemento na lista com a função append '''

#  adicionando uma lista de outra forma
lista1.extend([2, 5, 6])
print(lista1)
'''como podemos observar foi adicionado os valores individualmente'''

#  podemos adicionar valores a lista informando o indice com a função insert
lista1.insert(3, 4)
print(lista1)

#  podemos juntar uma lista na outra de duas formas
#  lista1 += lista5
#  lista1.extend(lista5)
#  temos duas maneiras de realizar a operação
print(lista1)

#  se quizermos fazer a inversão da lista podemos utilizar o reverse
# lista1.reverse()
# lista5.reverse()
# print(lista1)
# print(lista2)
# podemos fazer de outra maneira
# print(lista1[::-1])
# print(lista5[::-1])
# em ambos os casos obteremos o mesmo resultado

#  para copiarmos uma lista na outra podemos fazer
lista6 = lista2.copy()
print(lista6)

#  para sabermos o tamanho de uma lista basta usar o len
print(len(lista1))

# podemos remover o ultimo elemento da lista com o pop
print(lista5)
lista5.pop()
print(lista5)

# podemos remover os elementos usando o pop e passando o indice
print(lista1)
lista1.pop(4)
print(lista1)

# podemos remover todos os elementos da lista (zerar)
#print(lista1)
#lista1.clear()
#print(lista1)

# convertendo uma lista em uma string
nome = ['Curso', 'de', 'Python']
curso = ' '.join(nome)
print(curso)

# retorno do primeiro elemento do indice encontrado
print(lista1.index(9))

# algumas funções algebricas
nums = [2, 3, 5, 6, 6]
print(sum(nums))  # soma de todos os números da lista
print(max(nums))  # o maior número da lista
print(min(nums))  # o menor número da lista
print(len(nums))  # imprime o tamanho da lista

# transformando uma lista em tupla
num = [1, 3, 5, 6]
tupla = tuple(num)
print(num)
print(tupla)

# desempacotando listas
num1, num2, num3, num4 = num
print(num1)
print(num2)
print(num3)
print(num4)
