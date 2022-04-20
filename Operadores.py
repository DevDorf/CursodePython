# n1**(1/2) -> raiz
# print('='*20) -> faz print do igual 20 vezes, lado a lado
#nome = input('Qual é os eu nome? ')
#print('Prazer em te conhecer, {:=^20}!'.format(nome))
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma vale {}, \n o produto vale {}, \n e a divisão é {:.3f}'.format(s, m, d), end='> > >')
print('Divisão inteira {}, e a potência {}'.format(di, p))

#\n quebra de linha
#end='   ' continua na mesma linha
