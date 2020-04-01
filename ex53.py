frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separar formando listas
junto = ''.join(palavras) #junta todas as palavras sem espaço entre elas
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #vai varrer a string de tras pra frente
    inverso += junto[letra] # salvando letra por letra de tras pra frente
'''inverso = junto[::-1] # outra forma de varrer um string de tras pra frente'''
if inverso == junto:
    print('Temos um Palindromo.')
else:
    print('Não temos um Palindromo')
print(f'O inverso de {junto} é {inverso}.)