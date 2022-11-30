# faça um programa que leia um número qualquer e mostre o seu fatorial.
# primeiro resolução
''' num = int(input('digite um número: '))
f = 1
for i in range(num, 0, -1):
    f *= i
print(f'o fatorial de {num}! é {f}') '''



'''# segunda resolução com while
fat = 1
n = int(input('digite um número: '))
c = n
print(f'{n}! = ', end='')
while c > 0:
    fat *= c
    print(f'{c} x' if c > 1 else f'{c} = {fat}', end=' ')
    c -= 1'''

''' terceira resolução com função é recursividade
def fat(num):
    res = 1
    if num == 1 or num == 0:
        return 1
    return num * fat(num-1)

n = int(input('digite um número: '))
r = fat(n)
print(f'o fatorial de {n}! é igual a {r}')'''
