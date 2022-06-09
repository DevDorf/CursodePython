matriz1 = []
matriz2 = []
matriz3 = []
matriztot = []
for c in range(0, 3):
    matriz1.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    matriz2.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    matriz3.append(int(input(f'Digite um valor para [2, {c}]: ')))
matriztot.append(matriz1[:])
matriztot.append(matriz2[:])
matriztot.append(matriz3[:])
print('-=-' * 15)
for c in matriztot:
    print(f'{c} ')




