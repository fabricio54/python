# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('sexo: '))
while sexo not in 'FfMm':
    print('dados inválidos! tente novamente.')
    sexo = str(input('sexo: '))
print('dados válidos com secesso! ')
