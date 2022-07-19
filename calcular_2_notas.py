nota_1 = float(input("Entre com a primeira nota: "))
nota_2 = float(input("Entre com a segunda nota: "))

media = float(nota_1+nota_2) / 2

if media >= (7):
    print("Aprovado", round(media, 2))

if media <= (6.9):
    print("Reprovado", round(media, 2))
  
elif media == 10:
    print('Com Louvor!!')