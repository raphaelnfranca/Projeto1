from random import choice

n = int(input('Estou pensando em um número de 0 á 5, adivinhe qual é: '))

numeros = [1,2,3,4,5]

ne = choice(numeros)

if n==ne:
    print('Escolhi o {} VOCÊ ACERTOU!!!'.format(ne))

else:
    print('Errou!!!') 