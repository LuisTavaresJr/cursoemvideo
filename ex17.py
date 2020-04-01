import math
co = float(input('Comprimento do cateto aposto: '))
ca = float(input('Comprimento do cateto adjecente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
