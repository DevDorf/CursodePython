cont_idade = cont_F = cont_M = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite seu sexo [F\M]: ').strip().upper()[0]
    opcao = ' '
    while opcao not in 'NS':
        opcao = input('Você deseja continuar? [S/N] ').upper().strip()[0]

    print('=-=' * 15)
    if idade >= 18:
        cont_idade += 1
    if sexo == 'F' and idade < 20:
        cont_F += 1
    if sexo == 'M':
        cont_M += 1
    if opcao == 'N':
        print('-=-' * 15)
        print('Seus dados são:')
        break
print(f'''
Foram cadastradas:
{cont_idade} pessoas maiores de 18 anos.
{cont_M}  homens cadastrados.
{cont_F} mulheres menores de 20 anos.''')


