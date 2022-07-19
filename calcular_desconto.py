# Calcular desconto simples

valor = float(input(' Qual o preço do produto? '))

desconto = float(valor*0.05)
valor_liquido = float(valor-desconto)

print('O valor do produto com 5% de desconto é de R$ {}'.format(valor-desconto))