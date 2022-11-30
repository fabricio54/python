# 29: escreva um programa que leia a velocidade de um carro.se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada km acima do limite.
v = float(input('velocidade do carro: '))
multa = (v - 80) * 7
if v > 80:
    print('MULTADO! você excedeu o limite de 80Km/h.')
    print(f'a multa é de R${multa:.2f}')
    print(f'Tenha um bom dia!')
else:
    print('tudo norma por aqui!')
    print('dirija com cuidado!')
    print('tenha um bom dia!')