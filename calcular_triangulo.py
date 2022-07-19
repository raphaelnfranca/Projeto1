r1 = int(input('Primeiro número: '))
r2 = int(input('Segundo número:  '))
r3 = int(input('Terceiro número: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
  print('Você tem um triangulo.')

else:
  print('Você não tem um triangulo.')

