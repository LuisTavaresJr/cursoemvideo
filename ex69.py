quant = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('~'* 20)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continua: [S/N]')).upper().strip()[0]
    print('=-'* 20)
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if idade >= 18:
        quant += 1
    if opcao == 'N':
        break
print(f'Foi cadastrado {quant} pessoas com mais de 18 anos.')
print(f'Foi cadastrado {homem} Homens.')
print(f'Foi cadastrado {mulher} Mulheres com menos de 20 anos.')