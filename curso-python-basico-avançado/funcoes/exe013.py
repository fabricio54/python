# considere duas matrizes quadradas de ordem n. solicite uma linha e uma coluna e troque os valores da posição correspondente entre as matrizes. imprima as duas matrizes antes e depois da troca.
def criar_matriz(matriz, linha, coluna):
    for i in range(linha):
        matriz.append([0] * coluna)

def ler_matriz(matriz, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = int(input(f'mat[{i+1},{j+1}]: '))

def imprimir_matriz(matriz, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end=' ')
        print()

def troca_de_valores(matriz1, matriz2, linha, coluna):
    arma = 0
    for i in range(linha):
        for j in range(coluna):
            arma = matriz1[linha][coluna]
            matriz1[linha][coluna] = matriz2[linha][coluna]
            matriz2[linha][coluna] = arma

ordem = int(input('ordem da matriz: '))
mat1 = []
mat2 = []
criar_matriz(mat1, ordem, ordem)
criar_matriz(mat2, ordem, ordem)
print('lendo a primeira matriz: ')
ler_matriz(mat1, ordem, ordem)
print('lendo a segunda matriz: ')
ler_matriz(mat2, ordem, ordem)
print('primeira matriz: ')
imprimir_matriz(mat1, ordem, ordem)
print('segunda matriz: ')
imprimir_matriz(mat2, ordem, ordem)
print('informe uma linha e uma coluna respectivamente dentro do limite da matriz: ')
l = int(input('linha: '))
c = int(input('coluna: '))
troca_de_valores(mat1, mat2, l, c)
print('imprimindo as duas matrizes com as trocas feitas: ')
print('primeira matriz: ')
imprimir_matriz(mat1, ordem, ordem)
print('segunda matriz: ')
imprimir_matriz(mat2, ordem, ordem)