"""
Módulo collections - Counter (Contador)

collections -> High-perfomance Container Datatypes

Counter -> Recebe um interável e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro a como valor a quantidade de ocorrências desse elemento.

lista = [1, 1, 1, 1, 3, 3, 5, 5, 5, 6, 6, 6, 1, 1, 1, 2, 2, 2]

res = Counter(lista)

print(type(res))

print(res)

# Exemplo 2
print(Counter('Geek University'))

"""

# Utilizando o Counter

# Realizando o import
from collections import Counter

texto = (""" Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa.
 Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor,
  que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. Seu tamanho é variável.""").split()

print(Counter(texto))

# Podemos Calcular as repetições de palavras
