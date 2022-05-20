def multiplicacao(num, cont):
    multi = num * cont
    return multi
while True:
    num = int(input('Você quer ver a tabuada de qual numero? '))
    if num < 0:
        print('Programa de Tabuada encerrado!')
        break
    print('---' * 10)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {multiplicacao(num, cont)}')
    print('---' * 10)

