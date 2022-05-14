num = 0
doado = 1
while num != -1:
    num = float(input(''))
    doado += num
reais = doado * 2.50
print(f'VC$ {doado:.2f}')
print(f'R$ {reais:.2f}')
