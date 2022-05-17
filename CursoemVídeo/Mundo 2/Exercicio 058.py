from random import randint
jogador = 11
computador = 12
cont = 0
while computador != jogador:
    computador = randint(0, 10)
    jogador = int(input('Adivinhe o numero que o computador vai pensar entre 0 e 10:\n '))
    print('=-' * 20)
    print(f'O computador pensou no numero {computador}')
    print(f'O jogador escolheu o numero {jogador}')
    print('=-' * 20)
    if computador == jogador:
        print(f'O Jogador venceu! Você precisou de {cont} tentativas')
    else:
        cont += 1
        print('Infelizmente você não acertou, tente novamente')
        print('---' * 30)
