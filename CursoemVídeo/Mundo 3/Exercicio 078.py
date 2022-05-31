lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print('=-=-' * 15)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição', end=' ')
for pos, c in enumerate(lista):
    if c == maior:
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {menor} na posição', end=' ')
for pos, c in enumerate(lista):
    if c == menor:
        print(f'{pos}... ', end='')
