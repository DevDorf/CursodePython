r1 = float(input('Digite reta 1: '))
r2 = float(input('Digite reta 2: '))
r3 = float(input('Digite reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triangulo')
else:
    print('As retas não formam um triangulo ')

