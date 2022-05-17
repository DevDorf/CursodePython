resp = 0
while resp != 5:
    print('=-=' * 10)
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    print('###' * 13)
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')
    resp = int(input('Resposta: '))
    if resp == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é: {soma}')
    elif resp == 2:
        multi = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é: {multi}')
    elif resp == 3:
        if num1 > num2:
            print(f'O valor {num1} é maior que {num2}')
        else:
            print(f'O valor {num2} é maior que {num1}')
    elif resp == 4:
        print('Vamos de novo!')
    elif resp == 5:
        print('Fim do programa, Até a proxima!')
    else:
        print('Valor invalido')
