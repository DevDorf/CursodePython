contagem = 'zero', 'um', 'dois', ' tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente Novamente!', end=' ')
print(f'Você digitou o numero {contagem[escolha]}')
