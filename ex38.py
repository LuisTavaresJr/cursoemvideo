a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print('=-'*20)
print(f'Você digitou {a} e {b}. Vamos analisar!')
print('-='*20)
if a > b:
    print('O Primeiro valor é maior!')
elif b > a:
    print('O Segundo valor é o maior!')
else:
    print('Os dois valores são iguais!')
