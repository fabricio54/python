# crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.
nome = str(input('nome: ')).strip()
print(f'seu nome tem silva no nome ? {"silva"in nome.lower()}')