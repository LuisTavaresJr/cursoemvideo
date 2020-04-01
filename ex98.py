def contador(a, b, c):
    print(f'Contagem de {a} até {b} em {c}')
    if c == 2:
        c = -2
    for i in range(a, b, c):
        print(i, end=' ')
        if b > i:
            print('-> ', end='')
    print(' Fim!')

contador(1, 11, 1)
contador(10, 0, 2)