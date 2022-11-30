""" crie um progama que vai ler vários números e colocar em uma lista.
depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
 Ao final, mostre o conteúdo das três listas geradas."""

lista = []
lista2 = []
lista2.append([])
lista2.append([])
op = 's'
while op in 's':
    lista.append(int(input('digite um número: ')))
    op = str(input('deseja continuar ?'))
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        lista2[0].append(lista[i])
    else:
        lista2[1].append(lista[i])
print(f'lista como todos os números {lista}')
print(f'lista com os valores pares e ímpares {lista2}')
