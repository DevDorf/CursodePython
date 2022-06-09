pessoa = []
grupo = []
pesados = []
leves = []
contp = 0
while True: #Estrutura que adiciona os valores dentro das listas
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    contp += 1 #Contador de pessoas cadastradas
    resp = input('Quer continuar? [S/N]: ').strip()
    if resp in 'Nn':
        break
    elif resp not in 'NnSs':
        resp = input('Quer continuar? [S/N]: ').strip()

for pos in grupo:
    if pos == grupo[0]:
        maior = menor = pos[1]

    if pos[1] >= maior:
        maior = pos[1]
        pesados.append(pos[0])
    elif pos[1] <= menor:
        menor = pos[1]
        leves.append(pos[0])

print(f'O numero de pessoas cadastrdas foi: {contp}')
print(f'O maior peso foi de {maior}Kg. Peso de {pesados}')
print(f'O menor peso foi de {menor}Kg. Peso de {leves} ')
