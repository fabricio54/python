""" crie um progama onde o usuário digite uma expressão qualquer que use parênteses.
 seu aplicativo deverá analizar se a expressão passda está com os parênteses abertos e fechados na ordem correta."""

quant = 0

exp = str(input('escreva uma expressão: '))
for i in range(0, len(exp)):
    if exp[i] == '(':
        quant += 1
    if exp[i] == ')':
        quant -= 1
if quant == 0:
    print('a expressão está correta!')
else:
    print('a expressão está errada!')
