from random import randint
from time import  sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('JOKENPÔ')
print('==='*10)
print('''Faça a Sua Escolha:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua escolha?\n'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('==='*10)
print(f'O Computador escolheu {itens[computador]}')
print(f'O Jogador escolheu {itens[jogador]}')
print('###' * 10)

if computador == 0: # Computador Joga pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada Invalida')
elif computador == 1: # Computador joga papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada Invalida')
elif computador == 2: # Computador Joga tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida')