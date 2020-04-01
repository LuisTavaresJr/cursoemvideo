#peça ao cliente 3 comprimentos de retas e diga se elas formam um triangulo
print('Analisando Triângulo')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos a cima PODEM formar um triângulo!')
else:
    print('Os segmentos a cima NÃO podem forma um triângulo!')