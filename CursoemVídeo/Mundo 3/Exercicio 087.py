matriz1 = []
matriz2 = []
matriz3 = []
matriztot = []
soma = soma2 = maior = 0
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

for c in matriztot: # Estrutura para verificar os valores pares dentro da matriz e somar
    for num in c:
        if num % 2 == 0:
            soma += num
print(f'A soma dos valores pares digitados é: {soma}')
for c in matriztot: # Estrutura para verificar e somar valores na terceira coluna da matriztot
    for num in c:
        if num == c[2]:
            soma2 += c[2]
print(f'A soma dos valores na terceira coluna é: {soma2} ')
for c in matriztot[1]:
       if maior <= c:
           maior = c
print(f'O maior valor da segunda linha é: {maior}')
