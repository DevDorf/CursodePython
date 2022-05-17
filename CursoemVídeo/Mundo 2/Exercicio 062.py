primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
resp = 'S'
while resp != 0:
    for c in range(primeiro, decimo + razao, razao):
        print(c, end=' -> ')
    resp = int(input('Voce quer mostrar mais quantos termos? \n'))
    primeiro = c + razao
    decimo = primeiro + (resp - 1) * razao

