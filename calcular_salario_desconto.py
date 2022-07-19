# Calcular o Salário com desconto

ganhos = float(input('Quanto você ganha por hora? '))
hora_mes = float(input('Quantas horas você trabalha por mês? '))

soma = ganhos * hora_mes 

print('Salário bruto = R$', soma)

ir_soma = float(soma*0.11)
inss_soma = float(soma*0.05)
sindicato_soma = float(soma*0.05)
salario_liquido_soma = float(soma-ir_soma-inss_soma-sindicato_soma) 

print('IR = R$', round(ir_soma, 2))
print('INSS = R$', round(inss_soma, 2))
print('Sindicato = R$', round(sindicato_soma, 2))
print('Salário Liquido = R$', round(salario_liquido_soma, 2)) 