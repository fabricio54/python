# 17: faça um programa que leia o comprimento do cateto oposto e do cateto adjacente dej um triâgulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'a hipotenusa vai medir {hi:.2f}')