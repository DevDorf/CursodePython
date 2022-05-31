lista = input().split()

while True:
    resp = input()
    if resp == 'exibir':
        lista.sort()
        for c in range(0, len(lista)):
            print(f'{lista[c]}', end=' ')

    elif resp == 'adicionar':
        lista.append(input())

    elif resp == 'remover':
        remv = input()
        if remv not in lista:
            print(f'código {remv} não encontrado')
        else:
            lista.remove(input())

    elif resp == 'encerrar':
        lista.sort()
        for c in range(0, len(lista)):
            print(f'{lista[c]}', end=' ')
        break