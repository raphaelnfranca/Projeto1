# Calcular uso de tinta

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

tinta_litro = float(altura*largura/2)

print('Será necessário {} litros de tinta para pintar a parede.' .format(tinta_litro))
