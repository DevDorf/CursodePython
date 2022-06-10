from random import randint
from time import sleep
jogo = []
print('-=-' * 15)
print(f'Jogo da Mega')
print('-=-' * 15)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(qtd):
    for n in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    sleep(0.5)
    print(jogo)
    jogo.clear()
print('Espero ter ajudado, boa sorte!')
