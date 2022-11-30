# crie um progama que leia dois valores e mostre um menu como o ao lado na tela:
# seu programa deverá realizar a operação solicitada em cada caso.
''' [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do progama '''
from time import sleep

v1 = int(input('primeiro valor: '))
v2 = int(input('segundo valor: '))
opcao = 0
print('processando valores...')
sleep(1.5)
while opcao != 5:
    print('-='*22)
    print('''[ 1 ] somar
[ 2 ] multiplicar 
[ 3 ] maior 
[ 4 ] novos números
[ 5 ] sair do progame ''')
    opcao = int(input('informe a opção desejada: '))
    while 1 < opcao > 5:
        print('-=' * 22)
        print('opção inválida! tente novamente.')
        opcao = int(input('informe a opção desejada: '))
    if opcao == 1:
        print('-=' * 22)
        print('soma dos números: ')
        sleep(1)
        soma = v1 + v2
        print('-=' * 22)
        print(f'a soma de {v1} com {v2} é igual a {soma}')
    elif opcao == 2:
        print('-=' * 22)
        print('multiplicação dos números: ')
        multi = v1 * v2
        sleep(1)
        print('-=' * 22)
        print(f'a multiplicação entre {v1} e {v2} é igual a {multi}')
    elif opcao == 3:
        print('-=' * 22)
        print('o número maior: ')
        sleep(1)
        print('-=' * 22)
        if v1 > v2:
            print(f'o número {v1} é maior que {v2}')
        else:
            if v1 == v2:
                print(f'o número {v1} e {v2} são iguais')
            else:
                print(f'o número {v2} é maior que {v1}')
    elif opcao == 4:
        print('-=' * 22)
        print('novos números: ')
        sleep(1)
        print('-=' * 22)
        v1 = int(input('primeiro valor: '))
        v2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('-=' * 22)
        print('encerrando progama...')
        sleep(1.5)
print('progama encerrado com sucesso')
