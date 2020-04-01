# perguntar valor do salario e mostrar com aumento de 15%
salario = float(input('Digite o valor do seu salário: R$'))
novo = salario + (salario * 15/100)
print(f'Com o Aumento de 15% seu salário ficará R${novo:.2f}')