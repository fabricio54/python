""" tuplas (tuple)
    tuplas são bastantes parecidas com listas com algumas pequenas diferenças

    1. As tuplas são representadas por parenteses ().

    2. As tuplas são imutáveis: depois de criada náo podemos modificalas

    3. metodos para adição e remoção de valores nas tuplas não existem, dado o foto das tuplas serem imutáveis.

    4 . soma, valor máximo, valor mínimo, e tamanho.
    # se os valores forem todos inteiros ou reais
"""

tupla1 = (1, 4, 6, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 3, 5, 6
print(tupla2)

print(type(tupla2))

# gerando uma tupla com um range
tupla = tuple(range(11))
print(tupla)

# desempacotamento de tupla

tupla = ('Resident Evill 4', 'God of war')
jogo1, jogo2 = tupla
print(jogo1, jogo2)

# operações com tuplas
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

# convertendo um string para tupla
nome = tuple('rubacão com ovo')
print(nome)
print(nome.count('o'))  #contando quantas letras o tem na tupla