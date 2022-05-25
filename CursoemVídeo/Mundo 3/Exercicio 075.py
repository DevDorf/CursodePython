num = int(input('Digite um numero: ')), int(input('Digite um numero: ')),\
      int(input('Digite um numero: ')), int(input('Digite um numero: '))
print(f'Você digitou os valores {num}')
print(f'Foram encontrados {num.count(9)} valores 9')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram:')
for c in num:
    if c % 2 == 0:
        print(f'{c}', end=' ')
