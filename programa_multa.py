velocidade = float(input('Qual a velocidade do carro? '))

multa = (velocidade - 80)*7 

if velocidade <= 80:
  print('Sua velocidade é de {} km e está dentro da Lei.'.format(velocidade))

else:
  print('Sua velocidade é de {} e está acima da permitida, então sua multa é de: R$ {} '.format(velocidade, multa))