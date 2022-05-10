from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('JOKENPÔ')
print('==='*10)
print('''Faça a Sua Escolha:
Pedra
Papel
Tesoura''')
print('==='*10)

jogador = input('Qual sua escolha?\n').upper()


if computador == 'PEDRA' and jogador == 'PAPEL':
    print(f'Computador: {itens[computador]}\n Jogador: {jogador} \n Jogador VENCEU!!!')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print(f'Computador: {itens[computador]}\n Jogador: {jogador} \n Computador VENCEU!!!')
elif computador == 'PEDRA' and jogador == 'PEDRA':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n EMPATE')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n Computador VENCEU!!!')
elif computador == 'PAPEL' and jogador == 'TESOURA':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n Jogador VENCEU!!!')
elif computador == 'PAPEL' and jogador == 'PAPEL':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n EMPATE')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n Computador VENCEU!!!')
elif computador == 'TESOURA' and jogador == 'PEDRA':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n Jogador VENCEU!!!')
elif computador == 'TESOURA' and jogador == 'TESOURA':
    print(f'Computador: {itens[computador]} \n Jogador: {jogador} \n EMPATE')
elif jogador != 'TESOURA' and jogador != 'PEDRA' and jogador != 'PAPEL':
    print('Valor não reconhecido')


print('###' * 10)
print(f'O Computador escolheu: {computador}')
print((f'O Jogador escolheu: {jogador}'))
print('###' * 10)
