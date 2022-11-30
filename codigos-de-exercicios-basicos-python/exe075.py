""" crie um progama que ler vários números e coloca em uma lista. depois disso, mostre:
A) quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
op = 's'
aux = cont = 0
val5 = False

while op in 'sS':
    lista.append(int(input('digite um número: ')))
    if lista[cont] == 5:
        val5 = True
    op = str(input('quer continuar ?'))
    cont += 1


for i in range(0, len(lista)):
    for j in range(0, len(lista)):
        if lista[i] < lista[j]:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
print(f'foram digitados {cont} números')
print(f'valores da lista em ordem decrescente: {lista}')
if val5:
    print(f'o número 5 foi digitado')
else:
    print(f'o número 5 não foi digitado')
