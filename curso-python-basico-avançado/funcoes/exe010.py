# Questão 1. Faça um programa que leia uma matriz de dimensões determinadas pelo usuário. O programa deve imprimir a matriz informada e a transposta dessa matriz. Transposta é a matriz na qual linhas se tornam colunas e colunas se tornam linhas. (6,0 pontos)
def criar_matriz(matriz, linhas, colunas):
    for i in range(linhas):
        matriz.append([0] * colunas)

def ler_matriz(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = int(input(f'matriz[{i+1},{j+1}]: '))

def imprimir_matriz(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            print(matriz[i][j], end=' ')
        print()

def matriz_trasposta(matriz, linha, coluna):
    for i in range(coluna):
        for j in range(linha):
            print(matriz[j][i], end=' ')
        print()


print('informe um número de linhas e colunas respectivamente: ')
l = int(input('número de linhas: '))
c = int(input('números de colunas: '))
mat = []
criar_matriz(mat, l, c)
print('lendo a matriz: ')
ler_matriz(mat, l, c)
print('matriz: ')
imprimir_matriz(mat, l, c)
print('matriz trasposta: ')
matriz_trasposta(mat, l, c)
