# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

''' desenvolva um progama que leia o nome, idade e sexo de 4 pessoas. No final do progama, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

nome = ''
media = mulheres_20 = soma = idade_velho = 0
nome_mais_velho = ''
sexo = ''

for i in range(1, 5):
    print(f'<<<< PESSOA {i} >>>>')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    soma += idade
    sexo = str(input('sexo: [M/F]'))
    while sexo not in 'FfMm':
        sexo = str(input('sexo: [M/F]'))
    if sexo in 'Ff' and idade < 20:
        mulheres_20 += 1
    if sexo in 'Mm' and idade_velho < idade:
        nome_mais_velho = nome
        idade_velho = idade

media = soma / 4
print(f'foram informados dados de 4 pessoas.\na média de idade entre eles eh {media:.1f} anos \no homem mais velho tem {idade_velho} anos e se chama-se {nome_mais_velho}\nno grupo tem {mulheres_20} mulheres com menos de 20 anos.')
