num = int(input('Digite um número para ver sua tabuada: '))
for calculo in range(1, 11):
    print('{} x {:2} = {}'.format(num, calculo, num*calculo))