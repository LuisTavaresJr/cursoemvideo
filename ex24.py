# saber se na cidade digitada começa com a palavra Santo
cidade = str(input('Digite o nome da sua Cidade: '))
dividido = cidade.upper().split()
if dividido[0] == 'SANTO':
    print('A sua cidade começa com a palavra Santo!')
else:
    print('A sua cidade não começa com a palavra Santo!')
