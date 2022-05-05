velovidade = float(input("Qual a velocidade do carro? [km/h] "))
if velovidade > 80:
    multa = (velovidade - 80) * 7
    print('Você ultrapassou o limite, sua multa é de: R$ {:.2f}'.format(multa))
print('Você estava no limite de velocidade!')
