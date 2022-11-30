# leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
def criar_matriz(matriz,linha, coluna):
    for i in range(linha):
        matriz.append([0] * coluna)

def ler_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = int(input(f'matriz[{i+1},{j+1}]: '))

def imprimir_matriz(matriz,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end=' ')
        print()

def quant_valor(matriz,linha,coluna,valor):
    cont = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] > valor:
                cont += 1
    return cont

mat = []
l = 4
c = 4
v = 10
criar_matriz(mat, l, c)
print('lendo matriz: ')
ler_matriz(mat, l, c)
imprimir_matriz(mat, l, c)
soma = quant_valor(mat, l, c, v)
print(f'na matriz informada tem {soma} elementos maiores que 10')
