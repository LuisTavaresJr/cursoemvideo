sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor infome seu sexo [M/F]:')).strip().upper()[0]
print('dados atualizados')