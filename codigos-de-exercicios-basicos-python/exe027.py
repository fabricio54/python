# 27: faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Sousa
# primeiro = Ana
# último = Sousa
nome = str(input('digite seu nome completo: ')).upper()
print(f'seu nome completo é {nome}')
lista = nome.split()
print(f'o seu primeiro nome é {lista[0]}')
print(f'o seu último nome é {lista[-1]}')