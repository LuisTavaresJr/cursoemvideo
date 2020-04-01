nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome com todas letras maiúsculas fica {nome.upper()}.')
print(f'Seu nome com todas as letras minúsculas fica {nome.lower()}.')
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))


