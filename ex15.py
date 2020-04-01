# custo do aluguel é 60 reais por dia e 0.15 por km rodado

dias = int(input('Quantos dias ficou com o carro: '))
km = float(input('Quantos Km você rodou: '))
cdias = dias * 60
ckm = km * 0.15
total = cdias + ckm
print(f'Seu custo por dias foi R${cdias}!\nCusto por Km² R${ckm}!\nCom total a pagar de R${total}')
