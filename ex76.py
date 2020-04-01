lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99)
print('=-'* 15)
print(f'{" Listagem de preço ":-^30}')
print('=-'* 15)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<20}',end=' ')
    else:
        print(f'R${lista[i]:>7.2f}')