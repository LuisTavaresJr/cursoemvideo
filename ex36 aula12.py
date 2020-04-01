print('Emprestimo Bancario')
valor = float(input('Qual valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
ano = int(input('Pagar em quantos anos: '))
tempo = ano * 12
prestacao = valor / (ano * 12)
t = salario * 30 / 100
if prestacao < t:
    print(f'Parabéns seu emprestimo foi aprovado!\nFicou {tempo} prestações de R${prestacao:.2f}!')
else:
    print('Sinto muito, não foi aprovado!\nO valor da prestação passou de 30% do seu salário')
    print(f'Valor da prestação R${prestacao:.2f}.\n30% do seu salário R${t:.2f}.')