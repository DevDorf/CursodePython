cadastro = []
cont = soma = 0
while True:
    pessoa = {'nome': input('Nome: '), 'sexo': input('Sexo[M/F]: '), 'idade': int(input('Idade: '))}
    cadastro.append(pessoa)
    cont += 1
    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break

print('---' * 20)
print(f'- O grupo tem {cont} pessoas.')
for c in range(0, cont): #calculo da media
    num = cadastro[c]['idade']
    soma += num
media = soma / cont
print(f'- A média de idade é de: {media}')
print('- As mulhere cadastradas foram: ', end='')
for c in range(0, cont):
    totm = cadastro[c]['sexo']
    if totm in 'Ff':
        print(f'{cadastro[c]["nome"]}', end=', ')
print('\n')
print('- Lista das pessoas que estão acima da média:')
for c in range(0, cont):
    if cadastro[c]['idade'] > media:
        print(cadastro[c])
print()
print('Fim do programa')


