# 10 conversor de moedas: crie um progama que leia quanto de dinheiro uma pessoa tem de dinheiro na carteira e fassa a conversão de quanta daria em dolar: levando em conta que o dolar está a UR$ 3,60
real = float(input('quanto de dinhaeiro você tem na carteira ?'))
dolar = 3.60
con = real / dolar
print(f'R${real} reais da para comprar UR${con:.2f} dólares')
print(f'o dolar atualmente estando a UR${dolar}')