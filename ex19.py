import random
a1 = [str(input('Digite o nome do primeiro aluno: '))], [str(input('Digite o nome do segundo aluno: '))], \
     [str(input('Digite o nome do terceiro aluno: '))], [str(input('Digite o nome do quarto aluno: '))]
escolhido = random.choice(a1)
print(f'O aluno escolhido foi {escolhido}')
