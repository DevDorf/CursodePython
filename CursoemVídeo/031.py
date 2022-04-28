distancia = int(input('Qual a distancia a ser percorrida? [km]'))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Você pagará {:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Você pagará {:.2f}'.format(passagem))
