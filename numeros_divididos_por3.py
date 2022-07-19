# Numeros divididos por 3

soma = 0
cont = 0

for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        soma += contagem
        cont += 1
        
print('A soma de todos os números é {} e são {} valores somados.' .format(cont, soma))        