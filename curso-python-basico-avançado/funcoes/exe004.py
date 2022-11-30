# questão 4: dado um vetor de tamanho n, de valores, verifique se os elementos nele contidos encontram-se em ordem crescente.
def ler_vetores(vetor, intervalo):
    for i in range(intervalo):
        vetor[i] = int(input(f'vetor na posição {i+1}: '))


def compara(vetor,intervalo):
    for i in range(intervalo-1):
        if not vetor[i] < vetor[i+1] and i < intervalo:
            return False
    return True

n = int(input('informe o tamanho do vetor: '))
vetor = [0] * n
ler_vetores(vetor, n)
print(vetor)
if compara(vetor, n):
    print('o vetor em questão, tem os seus elementos em ordem crescente')
else:
    print('o vetor em questão, não tem o seu formato em ordem crescente')
