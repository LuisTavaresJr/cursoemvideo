print('Aumento de salário')
salario = float(input('Qual o seu salário: R$'))
if salario > 1250:
    aumento = salario + (salario * 10/100)
    print(f'Com o aumento de 10%, seu salário atual é R${aumento}.')
else:
    aumento = salario + (salario * 15/100)
    print(f'Com o aumento de 15%, seu salário atual é R${aumento}')
print('Obrigado e volte Sempre!')
