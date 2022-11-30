# 23 faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
num = int(input('digite um número entre 0 e 9999: '))
milhar = num // 1000
resto = num % 1000
centena = resto // 100
resto = resto % 100
dezena = resto // 10
resto = resto % 10
unidade = resto // 1
print(f'o número digitado foi {num}: ')
if num >= 1000:
    print(f'seu milhar foi: {milhar}')
if num >= 100:
    print(f'sua centena foi: {centena}')
if num >= 10:
    print(f'sua dezena foi: {dezena}')
print(f'sua unidade foi: {unidade}')