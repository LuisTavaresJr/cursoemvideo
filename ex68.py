from random import randint
print('Vamos jogar PAR ou ÍMPAR')
print('-'*60)
vitorias = 0
while True:
    n = int(input('Vamos jogar. Digite um valor: '))
    computador = randint(0, 10)
    total = n + computador
    opcao = ' '
    while opcao not in 'IP':
        opcao = str(input('Par ou Ímpar: [P/I]')).upper().strip()[0]
    print(f'Você jogou {n} e o computador jogou {computador}. Total foi {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    print('~'* 30)
    if opcao == 'P':
        if total % 2 == 0:
            print('Parabéns você venceu.')
            print('-='*30)
            vitorias += 1
        else:
            print('Game Over! Você Perdeu !')
            print('-='*30)
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Parabéns você venceu.')
            print('=-'*30)
            vitorias += 1
        else:
            print('Game Over! Você Perdeu.')
            print('-='*30)
            break
    print('Vamos continuar...')
print(f'Você teve {vitorias} vitorias!')