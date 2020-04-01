time = []
dados = {}
partidas = []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f'Quantos gols na {p}ª partida: ')))
    dados['gols'] = partidas[:]
    dados['Total'] = sum(partidas) # Faz uma soma da lista partidas
    time.append(dados.copy())
    while True:
        reps = str(input('Quer Continuar: [S/N]')).upper().strip()[0]
        if reps in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if reps in 'N':
        break
print('-='* 30) # daqui pra cima ler os dados dos jogadores
print('Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-='* 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='* 30)
while True:
    busca = int(input('Mostrar dados de qual jogador:[999 p/ parar]  '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Erro! Não exite jogador com codigo {busca}.')
    else:
        print(f'----- Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-=' * 30)
print('<<< Volte Sempre! >>>')