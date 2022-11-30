# desenvolva um progama que leia o nome, idade e sexo de 4 pessoas. no final do progama, mostre:
# ==> a média de idade do grupo.  ==> quantas mulheres têm menos 20 anos  ==> qual o nome do homem mais velho
nome = ''
idade = 0
sexo = ''
media = m20 = soma = 0
nome_mais_velho = ''
idade_mais_velho = 0
for i in range(0, 5, 1):
    nome = str(input("nome: "))
    idade = int(input("idade: "))
    sexo = str(input("sexo: [F/M]"))
    while sexo not in 'FfMm':
        print("dado inválido tente novamente!")
        sexo = str(input("sexo: [F/M]")).strip()[0]
    soma += idade
    if i == 0:
        idade_mais_velho = idade
        nome_mais_velho = nome
    elif idade_mais_velho < idade:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade > 20:
        m20 += 1
media = soma / 4
print(f""" a media de idade do grupo é de {media:.2f}
no grupo tem {m20} de mais de 20 anos de idade
o homem mais velho tem {idade_mais_velho} anos e chama-se {nome_mais_velho}""")
