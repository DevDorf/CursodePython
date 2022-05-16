inicio = int(input())
fim = int(input())
primo = 0
for c in range(inicio, fim + 1):
    if inicio % c == 0:
        print(inicio)
        primo += 1
        inicio += 1
print('primos: ', primo)
