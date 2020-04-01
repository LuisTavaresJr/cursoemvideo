def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    if idade < 16:
        return f'Com {idade} anos: Voto não Obrigatorio!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opsional!'
    else:
        return f'Com {idade} anos: Voto Obrigatorio!'


print('-' * 20)
ano = int(input('Em que ano você nasceu: '))
print(f'{voto(ano)}')