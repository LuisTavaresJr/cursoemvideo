frase =  str(input('Digite uma Frase: ')).strip().upper()
print('Na sua frase a letra A aparece {} vezes.'.format(frase.count('A')))
print('Aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))