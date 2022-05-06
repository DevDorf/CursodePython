print('--- Calculadora IMC ---')
peso = float(input('Digite o seu peso em Kg:\n'))
altura = float(input('Digite sua altura em m:\n'))

imc = (peso / altura) ** 2
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
