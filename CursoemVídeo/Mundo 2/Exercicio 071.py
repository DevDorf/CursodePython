cont_50 = cont_20 = cont_10 = cont_1 = 0
print('###' * 10)
print('###       Banco Dev        ###')
print('###' * 10)
saque = int(input('Qual valor você quer sacar? R$ '))
while True:
    if saque % 50 == 0:
        saque -= 50
        cont_50 += 1
    elif saque % 20 == 0:
        saque -= 20
        cont_20 += 1
    elif saque % 10 == 0:
        saque -= 10
        cont_10 += 1
    elif saque % 1 == 0:
        saque -= 1
        cont_1 += 1
    if saque == 0:
        break
print('###' * 15)
print(f'Total de {cont_50} de R$ 50')
print(f'Total de {cont_20} de R$ 20')
print(f'Total de {cont_10} de R$ 10')
print(f'Total de {cont_1} de R$ 1')
print('Obrigado por utilizar nosso banco!')






