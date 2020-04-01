print('Tabuada usando for!')
n = int(input('Qual número você quer saber a Tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
print('Fim')