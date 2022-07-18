# Jogo Jokenpô

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura ''')

jogador = int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(10
      )
print('-=' * 11)
print('O computador escolheu {}' .format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # Jogou pedra
    if jogador == 0:
        print('Empate!!!')
    elif jogador == 1:
        print('Jogador Venceu!!!')
    elif jogador == 2:    
        print('Computador Venceu!!!')
    else:
        print('Jogada Invalida!!!')    
elif computador == 1: # Jogou papel
    if jogador == 0:
        print('Computador Venceu!!!')
    elif jogador == 1:
        print('Empate!!!')
    elif jogador == 2:    
        print('Computador Venceu!!!')
    else:
        print('Jogada Invalida!!!')
elif computador == 2: # Jogou tesoura
    if jogador == 0:
        print('Jogador Venceu!!!')        
    elif jogador == 1:
        print('Computador Venceu!!!')
    elif jogador == 2:
        print('Empate!!!')
    else:
        print('Jogada Invalida')