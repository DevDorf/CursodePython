num1 = int(input())
num2 = int(input())
if num1 <= num2:
    for c in range(num1, num2 + 1):
        for pos in range(1, 11):
            print(f'{c} x {pos} = {c * pos}')
        print('--' * 5)
else:
    print('Nenhuma tabuada no intervalo!')