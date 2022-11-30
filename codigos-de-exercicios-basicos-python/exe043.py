# 43: desenvolva uma lógica que leia o peso e o peso e altura de uma pessoa, calcula seu índice de massa corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# -IMC abaixo de 18,5: abaixo do peso;
# -entre 18,5 e 25: peso ideal;
# -25 até 30: sobrepeso;
# -30 até 40: obesidade;
# -acima de 40: obesidade mórbida.
altura = float(input('informe sua altura: '))
peso = float(input('informe seu peso: '))
imc = peso / (altura ** 2)
if imc < 18:
    print(f'seu imc está em {imc:.1f} portanto está ABAIXO DO PESO.')
elif imc <= 25:
    print(f'seu imc está em {imc:.1f} portanto está com PESO IDEAL.')
elif imc <= 30:
    print(f'seu imc está em {imc:.1f} portanto está com SOBREPESO.')
elif imc <= 40:
    print(f'seu imc está em {imc:.1f} portanto está com obesidade.')
else:
    print(f'seu imc está em {imc:.1f} portanto está com obesidade morbida.')