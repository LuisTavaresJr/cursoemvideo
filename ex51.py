primeiro = int(input('Digite o número: '))
razao = int(input('Digite a Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU!')