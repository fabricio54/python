# crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário sse ele quer ou não continuar e digitar valores

num = c = mai = men = soma = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('digite um número: '))
    if c == 0:
        mai = men = num
    else:
        if mai < num:
            mai = num
        if men > num:
            men = num
    soma += num
    c += 1
    resp = str(input('quer continuar ? [S/N]'))
print(f'foram digitados {c} números;\n a soma entre eles foi {soma};\n o maior número foi {mai} o menor {men}.')
