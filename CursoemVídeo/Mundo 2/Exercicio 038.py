num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo valor é maior')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('Não foi pra isso que eu fui inventado!')
