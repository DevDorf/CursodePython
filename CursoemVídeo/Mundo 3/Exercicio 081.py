lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Você quer continuar? [S/N]').upper().strip()
    if resp in 'Nn':
        break
print('=-=-' * 15)
print(f'Foram digitado um total de {len(lista)} numeros')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não esta na lista')
