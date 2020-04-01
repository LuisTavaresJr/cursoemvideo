def area(a, b):
    total = a * b
    print(f'A área de um terreno de {a}x{b} é de {total}m²')


print('Controle de Terrenos')
lar = float(input('Largura (m) '))
comp = float(input('Comprimento (m) '))
area(lar, comp)