print('Tabela do Brasileirão 2018')
tabela = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético', \
         'Atlético PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', \
         'Corinthians', 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport', 'America MG', \
         'EC Vitória', 'Paraná'
print('='* 30)
print(f'Tabela do Brasileirão 2018: {tabela}')
print('='* 30)
print(f'Os 5 primeiros são : {tabela[:5]}')
print('='* 30)
print(f'Os 4 Últimos são: {tabela[-4:]}')
print('='* 30)
print(f'A tabela em ordem Alfabética: {sorted(tabela)}')
print('='* 30)
print(f'A Chapecoense está na posição: {tabela.index("Chapecoense")+1}ª')