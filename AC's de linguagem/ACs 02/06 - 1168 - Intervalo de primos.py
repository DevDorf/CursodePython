inicio = int(input())
fim = int(input())
primo = divisor = 0
for c in range(inicio, fim + 1):
    for x in range(1, c):
        if c % x == 0:
            divisor += 1
    if divisor == 1:
        primo += 1
        print(c)
    divisor = 0
print(f'primos: {primo}')
