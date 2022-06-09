pares = []
impares = []
todos = []

for c in range(1, 8):
    numero = int(input(f'Digite {c}° numero: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
pares.sort()
impares.sort()
todos.append(pares[:])
todos.append(impares[:])
print(f'Os valores pares digitados foram: {todos[0]}')
print(f'Os valores impares digitados foram: {todos[1]} ')
