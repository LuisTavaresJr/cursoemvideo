#descubra se o ano é bissexto
from datetime import date
print('Analisando se o ano é Bissexto ! Ou digite 0 para o ano ATUAL!')
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')
