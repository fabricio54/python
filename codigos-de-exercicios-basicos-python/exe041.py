# 41: a confederação nacional de natação precisa de um programa que leia o anoo de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -até 9 anos: mirim;
# -até 14 anos: infatil;
# -até 19 anos: júnior;
# -até 25 anos: sênior;
# -acima de 25 anos: master.
from datetime import date
ano_atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = ano_atual - nascimento
if idade <= 9:
    print(f'com {idade} ano(s) de idade está classificado como: MIRIM')
elif idade <= 14:
    print(f'com {idade} ano(s) de idade está classificado como: INFATIL')
elif idade <= 19:
    print(f'com {idade} anos(s) de idade está classificado como: JÚNIOR')
elif idade <= 25:
    print(f'com {idade} ano(s) de idade está classificado como: SÊNIOR')
else:
    print(f'com {idade} ano(s) de idade está classificado como: MASTER')