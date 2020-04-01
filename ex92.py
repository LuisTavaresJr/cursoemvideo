from datetime import date
from time import sleep
anotacao = {}
anotacao['nome'] = str(input('Nome: '))
atual = date.today().year
ano = int(input('Ano de nascimento: '))
anotacao['idade'] = atual - ano
anotacao['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
if anotacao['ctps'] != 0:
    anotacao['contratação'] = int(input('Ano de contratação: '))
    anotacao['salário'] = float(input('Salário: R$'))
    anotacao['Aposentadoria'] = anotacao['idade'] + ((anotacao['contratação'] + 35) - atual)
print('-=' * 30)
for k, v in anotacao.items():
    print(f'- {k} tem o valor {v}.')
    sleep(0.5)
