# exercicio 35: desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
med1 = float(input('informe a primeira medida: '))
med2 = float(input('informe a segunda medida: '))
med3 = float(input('informe a terceira medida: '))
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med2 + med1:
    print('com as medidas informadas da para se formar um triângulo')
else:
    print('com as medidas informadas não da para se formar um triângulo')