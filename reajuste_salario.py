valor = float(input(' Qual o salário? '))

aumento = float(valor*0.15)
valor_liquido = float(valor+aumento)

print('Salário com reajuste de 15% é de R$ {}'.format(valor_liquido))