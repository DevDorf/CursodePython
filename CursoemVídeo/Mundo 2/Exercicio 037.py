print('====== CONVERSOR ======')
num = int(input('Digite um numero: '))
print('==' * 12)
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
base = input('')
print('==' * 12)
if base == '1':
    binario = bin(num)
    print('O numero ', num, f' convertido para binário fica: {binario[2:]}')
elif base == '2':                   #[2:] serve para retirar as referencias dos resultados
    octal = oct(num)
    print('O numero ', num, f'convertido para octal fica: {octal[2:]}')
elif base == '3':
    hexadecimal = hex(num)
    print('O numero', num, f'convertido para hexadecimal fica {hexadecimal[2:]}')
else:
    print('valor inserido não reconhecido')
