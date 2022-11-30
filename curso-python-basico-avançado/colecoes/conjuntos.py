"""
Conjuntos
 - Conjuntos em qualquer linguagem de progamação, estamos fazendo referência a Teoria dos conjuntos da Matemática.

 - Aqui no Python, os conjuntos são chamados de Sets.

 Dito isto, da mesma forma que na matemática:

 - Sets (conjuntos) não possuem valores duplicados;
 - Sets (conjuntos) não possuem valores ordenados;
 - Valores nõa são acessados via índice, ou seja, conjuntos não são indexados;

 Conjuntos são bons para se utilizar quando precisamos armazenar elementos
 mas não nos importamos com a ordenação deles. quando não precisamos se preucupar
 com chaves, valores e items duplicados.

 Os conjuntos (sets) são referenciados em Python com chaves {}

 Diferença entre Conjuntos (Set) e Mapas (Dicionários) em python:
    - Um dicionário tem chave/valor;
    - um conjunto tem apenas valor;

    # definimos um conjunto:

# forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # temos valores repetidos
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará do conjunto.

# forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# usos interesantes com sets
# Imagine que fizemos em formulário um formulário de cadastro de visitantes em uma feira ou museu e os visitantes

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# importante lembrar que, além de não termos valores duplicados, não temos ordem
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'tuplas: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, ])

# usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informa manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, já que em que uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um llop na lista....?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4) # elemento ja existe no conjunto portando não eh adicionado
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  #  Não é indice Informamos o valor a ser removido.

print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro removido.

# Forma 2

s.discard(2)

print(s)

"""

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso python e um
# contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# veja que alguns alunos que estudam python tambem estudam java.

# precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)