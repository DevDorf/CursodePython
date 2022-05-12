primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' -> ')
print('acabou')
