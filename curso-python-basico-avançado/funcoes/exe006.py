# faça um programa que leia uma matriz quadrada de ordem n, informe se a matriz é considerada identidade.
# 1 0 0
# 0 1 0
# 0 0 1
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

def eh_identidade(matriz, linha, coluna):
    for i in range(linha):
        for j in range(coluna):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True

ordem = int(input('ordem da matriz: '))
mat = []
criar_matriz(mat, ordem, ordem)
print('lendo a matriz: ')
ler_matriz(mat, ordem, ordem)
print('matriz: ')
imprimir_matriz(mat, ordem, ordem)
if eh_identidade(mat, ordem, ordem):
    print('a matriz informada é considerada identidade')
else:
    print('a matriz informada não é considerada identidade')
