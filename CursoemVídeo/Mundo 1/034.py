salario = float(input('Digite seu salário: R$ '))
if salario >= 1250.00:
    aumento = (salario * 10 / 100) + salario
    print('Seu salário é de {}'.format(aumento))
else:
    aumento = (salario * 15 / 100) + salario
    print('Seu salario é de : {}'.format(aumento))
