# questão 2: Faça um programa que leia n valores para um vetor. Verifique se há elementos repetidos no vetor e os imprima.
def ler_vetor(vetor, n):
    for i in range(n):
        vetor[i] = int(input(f'elemento {i+1} do vetor: '))         # função criada para ler o vetor indicado


def ver_valor_repetido(lista, inicio, fim, vetor):
    for i in range(inicio, fim, 1):                                 # função criada exclusivamente para ver se temos valores repetidos, informando os parâmetros indicados, funciona tanto para olhar para frente como para traz.
        if lista[i] == vetor:
            return True
    return False

n = int(input('informe o número de elementos do vetor: '))
vetor = [0] * n
ler_vetor(vetor, n)
for i in range(n):
    if not ver_valor_repetido(vetor, 0, i-1 ,vetor[i]):            # aqui como a questão pede para olharmos se tem valores repetidos temos que, primeiro olharmos para traz se não teve, ai a condição entra, que no caso será outra condição para olharmos para frente ai podemos conferir se teve valores repetidos.
        if ver_valor_repetido(vetor, i+1, n-1, vetor[i]):
            print(f'o valor {vetor[i]} se repete')