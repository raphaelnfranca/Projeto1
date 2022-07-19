# Calcular Download

download = float(input('Qual o tamanho do Download em MB? '))
link_internet = float(input('Qual a velocidade do Link em Mbps? '))

minutos = (download/link_internet)

print('O tempo de download em minutos é de:', float(round(minutos)))