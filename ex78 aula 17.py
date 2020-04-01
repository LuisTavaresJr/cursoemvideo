valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou {valores}')
print('-='* 15)
print(f'O maior valor foi {max(valores)} na posição', end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print(f'\nO menor valor foi {min(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')