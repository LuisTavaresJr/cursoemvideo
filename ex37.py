n = int(input('Digite um número: '))
print('''Em qual base de conversão deseja conveter:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Qual opção: '))
if opcao == 1:
    print(f'{n} Convertido para BÍNARIO é {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} Convertido para OCTAL é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} Convertido para HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Opção Errada!')