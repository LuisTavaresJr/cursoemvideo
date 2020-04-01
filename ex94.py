dados = []
pessoas = {}
cont = soma = 0
mulher = []
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo [M/F]')).upper()
    pessoas['Idade'] = int(input('Idade: '))
    if pessoas['Sexo'] in 'F':
        mulher.append(pessoas['Nome'])
    soma += pessoas['Idade']
    cont += 1
    dados.append(pessoas.copy())
    resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print('=-'* 30)
print(f'- O grupo tem {cont} pessoas.')
media = soma / cont
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram : {mulher}')
for i, v in enumerate(dados):
    if v['Idade'] >= media:
        print(dados[i])
print('fim')