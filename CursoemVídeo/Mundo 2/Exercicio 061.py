primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont < 10:
    print(primeiro, end=' -> ')
    primeiro += razao
    cont += 1
print('FIM')
