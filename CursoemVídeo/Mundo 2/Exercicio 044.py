valor = float(input('Qual o valor?\n'))
print('''[1] Para pagamento no dinheiro/cheque
[2] Para pagamento no cartão 1x
[3] Para pagamento no cartão 2x
[4] Para pagamento no cartão 3x ou mais''')
escolha = int(input('Qual sua escolha? '))

if escolha == 1:
    desconto = valor - (valor*10/100)
    print(f'Você irá pagar: R$ {desconto:.2f}')
elif escolha == 2:
    desconto = valor - (valor*5/100)
    print(f'Você ira pagar: R$ {desconto:.2f}')
elif escolha == 3:
    print(f'Voce irá pagar R$ {valor:.2f} e o valor da parcela é: R$ {valor/2:.2f}')
elif escolha == 4:
    parcelas = int(input('Qual o numero de parcelas?'))
    juros = valor + (valor * 20 / 100)
    print(f'Você irá pagar R$ {juros:.2f} e o valor da parcela é {parcelas}x de: R$ {juros/parcelas:.2f}')
else:
    print('Opção invalida de pagamento. Tente novamente')
