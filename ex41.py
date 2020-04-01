from datetime import date
print('Confederação Nacional de Natação!')
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria Mirim!')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na categoria Infantil!')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na categoria Junior!')
elif idade <= 25:
    print(f'Você tem {idade} anos e está na categoria Sênior!')
else:
    print(f'Você tem {idade} anos e está na categoria Master!')
