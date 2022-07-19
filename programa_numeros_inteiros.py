
soma = 0
cont = 0

for c in range(1, 7): 
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0: # Formula do calculo numeros pares   
        soma += num
        cont += 1

print('Você informou {} pares números e a soma foi {}'.format(cont, soma))