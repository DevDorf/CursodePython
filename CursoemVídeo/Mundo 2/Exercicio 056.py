media = 0
maior = 0
nomevelho = 0
menor = 0
for c in range(1, 5):
    print('---' * 4, f'{c}º pessoa', '---' * 4)
    nome = input('Digite seu nome: ').strip()
    idade = int(input(f'{nome} digite sua idade: '))
    sexo = (input('Digite seu sexo [M/F]: ')).strip()
    print('-=' * 10)
    media += idade / 4
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    elif sexo in 'fF' and idade < 20:
        menor += 1
print(f'A média das idade é {media:.0f}')
print(f'O {nomevelho} tem {maior} e é o mais velho dentre os três')
print(f'Existem {menor} mulheres com idade menor que 20 anos')
