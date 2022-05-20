from random import randint
cont = 0
print('-=-' * 20)
print('Jogo do Par ou Impar')
print('-=-' * 20)
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um numero: '))
    escolha = input('Você quer Par ou Impar? [P/I] ').upper().strip()[0]
    print('-=-' * 20)
    print(f'O computador escolheu o numero {computador}')
    soma = jogador + computador
    if soma % 2 == 0:
        result = 'Par'
        print(f'A soma entre os valores é {soma} e esse numero é {result}')
        print('-=-' * 20)
    else:
        result = 'Impar'
        print(f'A soma entre os valores é {soma} e esse numero é {result}')
        print('-=-' * 20)
    if escolha == result[0]:
        print('O jogador Venceu!')
        print('-=-' * 20)
        cont += 1
    else:
        print('O jogador perdeu')
        print('-=-' * 20)
        print(f'GAME OVER! Você venceu {cont} vezes!')
        break
