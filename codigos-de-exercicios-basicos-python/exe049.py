#refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('digite um número inteiro: '))
for i in range(1, 11, 1):
    print(f'{i} x {num} = {i*num}')
print()
print(f'tabuada do {num}!')