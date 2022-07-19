# Ano bixesto

ano = int(input('Qual o ano? '))

bi = ano % 4

if bi == 0:
  print('O ano {} é bixesto.'.format(ano))

else:
  print('O ano {} não é bixesto.'.format(ano))