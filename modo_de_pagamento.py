# Modo de Pagamento Descontos

pagamento = float(input('Entre com o valor do pagamento: R$ '))       # Entrada

a_vista = (pagamento*0.10)                                            # Calculos
cartao = (pagamento*0.05)
cartao_2x = (pagamento)
cartao_3x = (pagamento+a_vista*2)

pagamento_a_vista = (pagamento - a_vista)                             # Calculos
pagamento_cartao = (pagamento - cartao)
pagamento_cartao_2x = (pagamento)/2
pagamento_cartao_3x = (cartao_3x)/3

print('''--------------------------------------------------------------   
[ 1 ] - para pagamento à vista em dinheiro. \033[1;32m 10% de Desconto\033[m.
[ 2 ] - para pagamento à vista no cartão.   \033[1;32m 5% de Desconto\033[m.
[ 3 ] - para pagamento no cartão em 2x.     
[ 4 ] - para pagamento no cartão em 3x.     \033[1;31m 20% de Acréscimo\033[m.''')
print('--------------------------------------------------------------')                           # Menu do programa

menu = int(input('Selecione o método de pagamento de 1 a 4 =>  '))

if menu == 1:
    print('O valor é de R${} com pagamento a vista! Desconto de R${}' .format(pagamento_a_vista, a_vista))  

elif menu == 2:
    print('O valor é de R${} com pagamento em cartão! Desconto de R${}' .format(pagamento_cartao, cartao))

elif menu == 3:
    print('O valor é de R${} com pagamento em 2x no cartão! 2x parcelas de R${}' .format(cartao_2x, pagamento_cartao_2x))        

elif menu == 4:
    print('O valor é de R${} com pagamento em 3x no cartão! 3X parcelas de R${}' .format(cartao_3x, pagamento_cartao_3x))