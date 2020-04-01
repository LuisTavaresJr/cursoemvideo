print('{} Analizando notas! {}'.format('=-'*10, '=-'*10))
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi {media:.1f} .Estude mais! Você foi REPROVADO!')
elif media < 7:
    print(f'Sua média foi {media:.1f} . Você foi para RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media:.1f} . Parabéns você foi APROVADO!')