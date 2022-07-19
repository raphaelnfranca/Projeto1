
maior = 0
menor = 0
for peso in range(1, 6):
    pesototal = float(input('Peso da {} pessoa: '.format(peso)))
    if peso == 1:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso
            
        if peso > menor:
            meno = peso
            
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))                   