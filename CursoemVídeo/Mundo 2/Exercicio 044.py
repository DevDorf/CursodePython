valor = float(input('Qual o valor?\n'))
print('[1] Para pagamento no dinheiro/cheque.')
print('[2] Para pagamento no cartão 1x')
print('[3] Para pagamento no cartão 2x')
print('[4] Para pagamento no cartão 3x')
escolha = input()

if escolha == '1':
    desconto = valor - (valor*10/100)
    print(f'Você irá pagar: R$ {desconto:.2f}')
elif escolha == '2':
    desconto = valor - (valor*5/100)
    print(f'Você ira pagar: R$ {desconto:.2f}')
elif escolha == '3':
    print(f'Voce irá pagar R$ {valor:.2f} e o valor da parcela é: R$ {valor/2:.2f}')
elif escolha == '4':
    juros = valor + (valor*20/100)
    print(f'Você irá pagar R$ {juros:.2f} e o valor da parcela é: R$ {juros/3:.2f}')
