# faca um algoritimo que leia o preço de um produto e mostre com desconto de 5%

preco = float(input('Qual o preço do produto: R$'))
novo = preco - (preco * 5 / 100)
print(f'Seu produto com desconto de 5% ficou no valor de R${novo:.2f}')
