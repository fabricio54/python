from time import sleep
from random import randint
from datetime import date

palavras = (str(input('')), str(input('')), str(input()), str(input('')), str(input('')), str(input('')))
for i in range(0, len(palavras)):
    print(f'na palavra {palavras[i].upper()} temos ', end='')
    for j in range(0, len(palavras[i])):
        if palavras[i][j] in 'AaEeIiOoUu':
            print(f'{palavras[i][j]} ', end='')
    print()