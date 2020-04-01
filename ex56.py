somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print(f'--------{p}ª Pessoa ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idades: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade # guarda as idade somando
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        mulher += 1
mediaidade = somaidade / 4 # da a media da idade
print(f'A média de idade do grupo é de {mediaidade} anos. ')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos')
print(f'Teve {mulher} mulheres menor que 20 anos.')