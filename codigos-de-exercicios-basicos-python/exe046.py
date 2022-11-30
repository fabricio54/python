# 46:faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 a 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for i in range(10, 0, -1):
    sleep(0.5)
    print(i)
print('acabou!')