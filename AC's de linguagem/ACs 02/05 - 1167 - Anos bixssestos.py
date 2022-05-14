inicio = int(input())
fim = int(input())
biss = 0
while inicio < fim + 1:
    if inicio % 4 == 0 and inicio % 100 != 0:
        print(inicio)
        biss += 1
    inicio += 1
print(f'bissextos: {biss}')