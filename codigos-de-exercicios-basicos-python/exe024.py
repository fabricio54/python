# 24: crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cid = str(input('digite um nome de uma cidade: ')).upper().strip()
c = cid.split()
if c[0] == 'SANTO':
    print(f'a cidade de {cid} começa com o nome "Santo"')
else:
    print(f'a cidade de {cid} não começa com o nome "Santo"')