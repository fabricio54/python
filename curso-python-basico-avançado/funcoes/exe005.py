# faça um programa que leia duas matrizes de mesma dimensão.gere uma terceira matriz contendo a soma dessa duas matrizes, imprima todas as três.
def criar_matriz(matriz, linha, coluna):
    for i in range(linha):
        matriz.append([0] * coluna)

def ler_matriz(matriz, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = int(input(f'matriz[{i+1},{j+1}]: '))

def imprimir_matriz(matriz, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end=' ')
        print()
    print()

def soma_de_matrizes(matrizf, matriz1, matriz2, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            matrizf[i][j] = matriz1[i][j] + matriz2[i][j]

ordem = int(input('ordem da matriz: '))
mat = []
mat2 = []
matfin = []
criar_matriz(mat, ordem, ordem)
criar_matriz(mat2, ordem, ordem)
criar_matriz(matfin, ordem, ordem)
print('lendo a primeira matriz: ')
ler_matriz(mat, ordem, ordem)
print('lendo a segunda matriz: ')
ler_matriz(mat2, ordem, ordem)
soma_de_matrizes(matfin, mat, mat2, ordem, ordem)
print('primeira matriz: ')
imprimir_matriz(mat, ordem, ordem)
print('segunda matriz: ')
imprimir_matriz(mat2, ordem, ordem)
print('somas das matrizes: ')
imprimir_matriz(matfin, ordem, ordem)

