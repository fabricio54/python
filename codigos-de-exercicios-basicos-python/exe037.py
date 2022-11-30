# exercicio 37: ecreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário;
# -2 para octal;
# -3 para hexdecimal.
num = int(input('digite um número qualquer pelo teclado: '))
print(f'o número {num} convertido para BINÁRIO é {bin(num)}')
print(f'o número {num} convertido para OCTAL é {oct(num)}')
print(f'o número {num} convertido para HEXADECIMAL é {hex(num)}')