# crie um programa que leia vários números interiros pelo teclado,o progama só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no final, mostre quantos números foram digitados e qual foi a soma entre eles.

num = soma = quant = 0
while True:
    num = int(input('digite um número: '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'foram digitados {quant} números e a soma entre eles foi {soma}')
