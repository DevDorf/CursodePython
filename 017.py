from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor de cateto adjacente: '))
h = hypot(co, ca)
print('O valor da hipotenusa para os valores {} e {} é: {:.2f}'.format(co, ca, h))
