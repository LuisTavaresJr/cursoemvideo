dados = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        dados[0].append(n)
    else:
        dados[1].append(n)
print('-='* 30)
print(f'Todos os números digitados foi: {dados}')
print(f'Lista de números PARES: {sorted(dados[0])}')
print(f'Lista de números ÍMPARES: {sorted(dados[1])}')
