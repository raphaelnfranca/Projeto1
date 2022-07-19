a = float(input('Qual o primeiro número? '))
b = float(input('Qual o segundo número? '))
c = float(input('Qual o terceiro número? '))


numero = float(a)
numero_2 = float(b)
numero_3 = float(c)

if a > b > c:
  print('O maior número é ', numero)

if b > a > c:
  print('O maior número é ', numero_2)

elif c > b > a:
  print('O maior númeor é ', numero_3)
