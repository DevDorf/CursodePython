primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + 10 * razao
while primeiro < decimo:
    print(primeiro, end=' -> ')
    primeiro += razao
