# questão 3: faça um programa que leia dos vetores de mesmo tamanho, informado pelo usuário.imprima ambos e informe se eles são iguais, ou seja se possuem os mesmos  elementos, nas mesmas posições.
def vetor(vetor, intervalo):
    for i in range(intervalo):
        vetor[i] = int(input(f'vetor na posição {i+1}: '))
    print()

def comparar(vetor1, vetor2, tamanho):
    for i in range(tamanho):
        if vetor1[i] != vetor2[i]:
            return False
    return True

tam = int(input('informe o tamanho do vetor: '))
vet1 = [0] * tam
vet2 = [0] * tam
print('informe os elementos do primeiro vetor: ')
vetor(vet1, tam)
print('informe os elementos do segundo vetor: ')
vetor(vet2, tam)
print(f'primeiro vetor: {vet1}')
print(f'segunddo vetor: {vet2}')
if comparar(vet1, vet2, tam):
    print('os elementos dos vetores são iguais')
else:
    print('os elementos dos vetores não são iguais nas respectivas posições')