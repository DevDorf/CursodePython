frase = input('Digite uma frase:\n').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # inverso = junto[::-1] substitui o for
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')


