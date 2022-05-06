reta1 = float(input('Valor da primeira reta: '))
reta2 = float(input('Valor da segunda reta: '))
reta3 = float(input('Valor da terceira reta: '))

if ((reta1 + reta2) < reta3) and ((reta1 + reta3) < reta2) and ((reta2 + reta3) < reta1):
    print(f'As retas: {reta1}, {reta2} e {reta3}; não formam um triangulo')
elif reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
    print(f'As retas: {reta1}, {reta2} e {reta3}; formam um triangulo Equilátero')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print(f'As retas: {reta1}, {reta2} e {reta3}; formam um triangulo Isósceles')
else:
    print(f'As retas: {reta1}, {reta2} e {reta3}; formam um triangulo Escaleno')
