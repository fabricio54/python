# 16: crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
import math
num = float(input('digite um valor: '))
print(f'o valor digitado foi {num} e a sua morção inteira é {math.trunc(num)}')