from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano nasceu a {c}ª pessoa:  '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print(f'''O somatorio é:
Maior {maior}
Menor {menor}''')