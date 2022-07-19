# Contador lançamento fogos artificio

from time import sleep

print('Começando a contagem regressiva!!!')
print('-=' * 8)
for contagem in range (10 , 0, -1):
    sleep(1)
    print(contagem)
    
print('Lançamento!!!')