lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Foi adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista): #verifica em que posição ele vai colocar
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Foi adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=-=' * 15)
print(f'Os valores digitados em ordem foram {lista}')
