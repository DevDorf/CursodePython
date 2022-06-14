from random import randint
from time import sleep
jogador = {}
jogo = []
for c in range(1, 5):
    num = randint(1, 6)
    jogador['player'] = num
    jogo.append(jogador.copy())
    print(f'O {c}º jogador tirou: {num}')
    sleep(1)





print(jogo)


