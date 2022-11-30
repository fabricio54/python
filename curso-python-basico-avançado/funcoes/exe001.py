#questão 1:  faça um programa para imprimir os n primeiros números primos, onde o usuário informa o valor de n.
def eh_primo(numero):
    for i in range(2,numero):    # criamos essa função exclusivamente para testar se o número enviado é primo, se não for ele retornara como verdadeiro e se não retornara como falso.
        if numero % i == 0:
            return False
    return True


n = int(input('informe um valor n para os primeiros números primos: '))
numero = 1                                                                   # para esse codigo criamos um contador para laço ja que, a questão nos pede uma quantidade determinada de números que so pode ser aumentada comforme o for achando os números primos 
conta = 0
while conta < n:
    if eh_primo(numero):
        print(numero, end= ' ')
        conta += 1
    numero += 1