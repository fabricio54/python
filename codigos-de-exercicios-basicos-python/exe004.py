# 04 faça um progama que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre eles.
a = input('digite algo pelo teclado: ')
print(f'o tipo primitivo desse valor é {type(a)}')
print(f'so tem espaços ? {a.isspace()}')
print(f'é um número ? {a.isalnum()}')
print(f'é alfabético ? {a.isalpha()}')
print(f'é alpha númerico ? {a.isalnum()}')
print(f'esta maiscula ? {a.isupper()}')
print(f'esta minusculo ? {a.islower()}')
print(f'está capitalizada ? {a.istitle()}')