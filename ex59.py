n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while not opcao == 5:
    print(f'''O que você quer fazer com {n1} e {n2}:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa''')
    opcao = int(input('Qual sua Opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} tem como respota: {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A Multiplicação entre {n1} e {n2} tem como resposta: {mult}')
    if opcao == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}!')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print('Não tem maior ! Os dois números sao iguais!')
    elif opcao == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    print('-='* 30)
print('Obrigado e volte sempre!')
