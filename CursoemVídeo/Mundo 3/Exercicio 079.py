lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Adicionado com Sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!')
    resp = input('Quer continuar? [S/N]: ').upper().strip()
    if resp in 'Nn':
        break
print('-=-=' * 15)
lista.sort()
print(lista)

