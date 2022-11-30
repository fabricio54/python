# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o programa será interrompido quando o número solicitado for negativo.

num = int(input('informe um número para vermos sua tabuada: '))
for i in range(1,11, 1):
    print(f'{num} x {i} = {num*i}')
print()
print(f'tabuada do {num}!')