dados = []
pessoas = {}
soma = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]')).upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite M ou F!')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    dados.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N')
    if resp in 'N':
        break
print('=-'* 30)
print(f'- O grupo tem {len(dados)} pessoas.')
media = soma / len(dados)
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram : ', end='')
for p in dados:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}.', end='')
print()
print('Lista das pessoas que estão acima da média:')
for p in dados:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f' {k} = {v};', end='')
        print()
print('<<< ENCERRADO >>>')