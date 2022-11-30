# faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for i in range(1, 500, 1):
    if i % 3 == 0:
        soma += i
        print(f'\033[0;32m{i}\033[0m', end=' ')
    else:
        print(f'\033[0;31m{i}\033[0m', end=' ')
print()
print(f'a soma de todos os números de 1 a 500 que são múltiplos de 3 é {soma}')