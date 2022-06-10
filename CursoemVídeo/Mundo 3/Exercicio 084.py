pessoa = []
grupo = []
maior = menor = 0
while True: #Estrutura que adiciona os valores dentro das listas
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = input('Quer continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
    elif resp not in 'NnSs':
        resp = input('Quer continuar? [S/N]: ').strip()
print(f'O numero de pessoas cadastrdas foi: {len(grupo)}')
print(f'O maior peso foi de {maior}Kg', end=' ')
for c in grupo:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')
print()
print(f'\nO menor peso foi de {menor}Kg', end=' ')
for c in grupo:
    if c[1] == menor:
        print(f'[{c[0]}]', end=' ')
