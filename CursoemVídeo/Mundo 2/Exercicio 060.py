'''from math import factorial
num = int(input('Calcule o fatorial de: '))
f = factorial(num)
print(f'O fatorial de {num} é {f}')'''

num = int(input('Digite uma valor: '))
c = num
f = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

