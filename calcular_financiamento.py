# Calcular o financiamento

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
anos_pagamento = int(input('Quantos anos para pagar? '))

prestacao = (valor_casa // anos_pagamento/12) 

if prestacao <= (salario*0.30):
  print('Você pode financiar a casa! O valor da prestação é R${}.' .format(prestacao))

else:
  print('Você não pode financiar a casa!')
