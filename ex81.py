lista = []
while True:
    lista.append((int(input('Digite um valor: '))))
    r = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if r in 'N':
        break
print('-=' * 30)
print(f'Foi digitado {len(lista)} Elementos.')
lista.sort(reverse=True)
print(f'A lista em ordem Decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado em sua lista.')
else:
    print('O valor 5 não foi digitado em sua lista.')
