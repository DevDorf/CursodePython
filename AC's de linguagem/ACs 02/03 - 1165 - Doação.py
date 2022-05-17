num = float(input())
num = 0
doado = 0
while num != -1:
    doado += num
    num = float(input())
print(f'VC$ {doado:.2f}')
print(f'R$ {doado * 2.50:.2f}')
