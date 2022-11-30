# 11 pintando uma parede: leia o comprimento e altura de uma parede e calcule sua área, para pintar essa parede leva 2m da area leva um litro de tinta,calcule quantos litros de tinta leva para pintar a parede.
comprimento = float(input('comprimento: '))
altura = float(input('altura: '))
area = comprimento * altura
tinta = 0.5
tot_pit = area * tinta
print(f'a parede mede {altura}m de altura e {comprimento}m de comprimento')
print(f'a área total da parede é {area:.2f}m²')
print(f'para pintar essa parede leva {tot_pit:.2f}l de tinta')