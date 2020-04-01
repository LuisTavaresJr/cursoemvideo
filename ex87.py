matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # como ja sabe o numero de elementos ja declarou para nao ter que usar o append
par = soma = maior = 0
for l in range(0, 3): # vai pegar a primeira linha
    for c in range(0, 3): # vai percorrer a primeira linha adicionando os valores
        matriz[l][c] = int(input(f'Digite um valor para: [{l}][{c}] ')) # matriz vai receber os valores
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        soma += matriz[l][2]
print('-='* 15)
for l in range(0, 3): # mais um laço para poder mostrar na tela
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') # vai mostrar a matriz a primeria linha e pula pra baixo.
    print()
print('=-' * 15)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira colune é {soma}')
for c in range(0, 3): # descobrir o maior da linha[1]
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
