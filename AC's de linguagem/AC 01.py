preco = float(input())
quant = int(input())
val = preco * quant
descf = val*(10/100)
descq = (val*(1/100))*quant
valf = val - (descf + descq)
print('{:.2f}'.format(val))
print('{:.2f}'.format(valf))