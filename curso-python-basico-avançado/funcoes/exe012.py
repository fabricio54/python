# leia uma matriz 5 x 5.leia também um valor x. o progama deverá fazer uma busca automaticamente e no final, a localização (linha e coluna) ou a mensagem de não encontrado.
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

def encontrar_valor(matriz, linha, coluna, valor):
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == valor:
                print(f'o valor foi encontrado na linha {i+1} e coluna {j+1}')
                return True
    return False

mat = []
ordem = 3
criar_matriz(mat, ordem, ordem)
print('lendo matriz: ')
ler_matriz(mat, ordem, ordem)
print('imprimindo matriz: ')
imprimir_matriz(mat, ordem, ordem)
v = int(input('informe um valor um valor: '))
if encontrar_valor(mat, ordem, ordem, v):
    print()
else:
    print('valor não encontrado na matriz!')