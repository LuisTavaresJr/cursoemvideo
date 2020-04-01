print('Tabuadas')
print('Digite um número negativo pra parar o programa!')
while True:
    n = int(input('Qual número você quer ver a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('~'*20)

print('Tabuada finalizada!')
