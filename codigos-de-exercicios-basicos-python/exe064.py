# crei um programa que leia vários números inteiros pelo teclado. o progama só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no final, mostre quantos números foram digitados e qual foi a soma entre eles(desxonsiderando o flag)

# sem o break
'''
soma = cont = 0
num = 0
while num != 999:
    soma += num
    num = int(input('digite um número: [999 para parar ]'))
    if num != 999:
        cont += 1
print(f'foram no total {cont} números digitados e a soma entre eles foi {soma}')
'''

'''soma = cont = 0
num = 0
while True:
    soma += num
    num = int(input('digite um número: [999 para parar]'))
    if num == 999:
        break
    cont += 1
print(f'foram no total {cont} números digitados e a soma entre eles foi {soma}')'''
