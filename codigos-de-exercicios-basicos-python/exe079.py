""" crie um progama onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente."""

lista = []
lista.append([])
lista.append([])
op = 's'
aux = cont_p = cont_i = 0

for i in range(0, 7):
    num = int(input('informe um número: '))
    if num % 2 == 0:
        lista[0].append(num)
        for j in range(0, len(lista[0])):
            if lista[0][j] < lista[0][cont_p]:
                aux = lista[0][cont_p]
                lista[0][cont_p] = lista[0][j]
                lista[0][j] =

    else:
        lista[1].append(num)
