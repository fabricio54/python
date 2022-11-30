""" crie um progama que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

linhas = 3
colunas = 3
matriz = []

for i in range(linhas):
    matriz.append([0] * colunas)

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f'matriz{[i]}{[j]}: '))

for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end=' ')
    print()