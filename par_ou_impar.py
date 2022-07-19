numero = int(input('Digite o número: '))

resultado = numero % 2
if resultado > 0:
  print('{} é um número impar.'.format(numero))
else:
  print('{} é um número par.'.format(numero))