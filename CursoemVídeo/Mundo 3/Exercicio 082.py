lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Deseja Continuar? [S/N] ').upper().strip()
    if resp in 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-=-=' * 15)
print(f'Essa é a lista completa: {lista}')
print(f'Essa é a lista PAR: {par}')
print(f'Essa é a lista IMPAR: {impar}')