from datetime import date
print('Analisar sua idade para Alistamento militar.')
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade < 18:
    falta = 18 - idade
    a = falta + date.today().year
    print(f'Você tem {idade} anos.')
    print(f'Ainda não chegou no tempo de se Alistar, Faltam {falta} anos!')
    print(f'Você deverá se alistar em {a}.')
elif idade > 18:
    passou = idade - 18
    a = date.today().year - passou
    print(f'Você tem {idade} anos.')
    print(f'Já passou {passou} anos do tempo do seu alistamento!')
    print(f'Você deveria ter se alistado em {a} .')
else:
    print(f'Você tem {idade} anos.')
    print('Está na hora de se alistar no execito brasileiro!')
print('Obrigado !')