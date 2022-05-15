inicio = int(input())
fim = int(input())
primo = 0
while inicio < fim + 1:
    if inicio % inicio == 0:
        print(inicio)
        primo += 1
    inicio += 1
print('primos: ', primo)
