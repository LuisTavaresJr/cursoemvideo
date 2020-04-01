dados = {}
gol = []
dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for p in range(0, partidas):
    gols = int(input(f'Quantos gols na {p}ª partida: '))
    gol.append(gols)
dados['gols'] = gol
dados['Total'] = sum(gol) # Faz uma soma da lista gol
print('-='* 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(dados)
print('-='* 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')
for i, v in enumerate(gol):
    print(f'Na partida {i}, fez {v} gols.')
print(f'Com um total de {dados["Total"]} gols')