# 15:escreva um programa que pergunte a quntidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.calcule o preço a pagar, sabendo que o custa R$60 por dia e R$ por km redado.
km = float(input('quantidade de quilômetros rodados: '))
dias = int(input('quntidade de dias alugado: '))
total = (60*dias)+(km*0.16)
print(f'foram {km} rodados e {dias} dias alugado e o gasto total foi de R${total:.2f}')