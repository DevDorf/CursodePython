d = int(input('Por quantos dias você vai alugar o carro?'))
k = float(input('Quantos Km você pretende andar?'))
pago = (d * 60) + (k * 0.15)
print('Você ira precisar desenbolsar R${:.2f}'.format(pago))