# 18: faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ângulo = float(input('digite o ângulo que vocÇe deseja: '))
seno = sin(radians(ângulo))
print(f'o ângulo de {ângulo} tem o seu seno de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'o ângulo de {ângulo} tem o seu cosseno de {seno:.2f}')
tangente = tan(radians(ângulo))
print(f'o ângulo de {ângulo} tem a tangente de {tangente:.2f}')