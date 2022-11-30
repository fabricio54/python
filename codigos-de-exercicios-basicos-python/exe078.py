""" faça um progama que leia nome e peso de várias pessoas, gurdando tudo em uma lista. no final, mostre:
 A) quantas pessoas foram cadastradas.
 B) uma listagem com as pessoas mais pesadas.
 C) uma listagem com as pessoas mais leves
 """
lista = []
lista.append([])
lista.append([])
op = 's'
cont1 = mai = men = 0

while op in 'sS':
    lista[0].append(str(input('informe o nome: ')))
    lista[1].append(int(input('informe o peso: ')))
    if cont1 == 0:
        mai = men = lista[1][0]
    else:
        if mai < lista[1][cont1]:
            mai = lista[1][cont1]
        if men > lista[1][cont1]:
            men = lista[1][cont1]
    cont1 += 1
    op = str(input('quer continuar ?'))
print(f'foram cadastradas {len(lista[0])} pessoas')
if lista[1].count(mai) > 1:
    print(f'as pessoas mais pesadas ', end='')
    for i in range(0, lista[1].count(mai)):
        print(f'{mai}...')
else:
    print(f'o maior peso foi de {mai}')
if lista[1].count(men) > 1:
    print(f'as pessoas com os menores pesos foram ', end='')
    for i in range(0, lista[1].count(men)):
        print(f'{men}...')
else:
    print(f'o menor peso foi de {men}')