from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
jogador = int(input("Qual numero entre 0 e 5 eu estou pensando?"))
print('PROCESSANDO')
sleep(3)
if computador == jogador:
    print('Você acertou o numero, Parabens')
else:
    print('Ganhei, eu pensei no numero {}'.format(computador))
