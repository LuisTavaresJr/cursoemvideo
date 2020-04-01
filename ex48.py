soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # saber se o número é divisivel por 3
        soma += c # Acumulador normalmente soma valor
        cont += 1 # Contador normalmente conta mais 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')
