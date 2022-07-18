
# Programa Alistamento Militar 1.0v

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
  print('Você tem que alistar agora!')

elif idade < 18:
  resta = 18 - idade
  print('Ainda faltam {} anos para o alistamento.'.format(resta))
  ano = atual + resta
  print('Seu alistamento será20 em {}.'.format(ano))
