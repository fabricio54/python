# 39: faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,se é a hora exata de se alistar ou se já passou do tempo do alistamento.seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = date.today().year
data_nascimento = int(input('informe sua data de nascimento: '))
idade = ano - data_nascimento
if idade > 18:
    print(f'o candidato passou da idade mínima estabelecida para o alistamento militar. tendo-o passado {idade-18} ano(s)')
elif idade < 18:
    print(f'o candidato ainda não está listo para o serviço militar. faltando ainda {18 - idade} ano(s)')
else:
    print('já está na hora de se alistar no serviço militar.')