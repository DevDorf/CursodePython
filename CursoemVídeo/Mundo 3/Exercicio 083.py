exp = input('Digite a expressão: ')
pa = 0
pf = 0
for c in exp:
    for pos in c:
        if pos in '(':
            pa += 1
        if pos in ')':
            pf += 1
if pa == pf:
    print('Expressão válida')
else:
    print('Expressão Invalida')
