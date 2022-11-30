# 22: crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas al letras maiúsculas e minúsculas.
# quantas letras ao todo (sem considerar espaços)
# quantas letras tem o primeiro nome.
nome = str(input('nome: ')).strip()
print(f'o nome em maiúsculas é {nome.upper()}')
print(f'o nome em minúsculas é {nome.lower()}')
total = (len(nome) - nome.count(' '))
print(f'o total de letras do nome é {total}')
#print('seu primeiro nome tem {nome.find(' ')} letras')
separa = nome.split()
print(f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')