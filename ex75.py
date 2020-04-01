n = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))
print(f'Você Digitou : {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares foram ',end='')
for c in n:
    if c % 2 == 0:
        print(f'{c}, ', end='')