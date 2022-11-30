# exercicio 30: crie um programa que leia um número e mostre na tela se ele é par ou impar.
num = int(input('digite um número: '))
if num % 2 == 0:
    print(f'o número {num} é par.')
else:
    print(f'o número {num} é impar.')