entrada1 = input().split()
entrada2 = input().split()
mult1 = float(entrada1[1])
mult2 = float(entrada2[1])
valor1 = float(entrada1[2])
valor2 = float(entrada2[2])
tot1 = mult1 * valor1
tot2 = mult2 * valor2
totfinal = tot1 + tot2
print(f'VALOR A PAGAR: R$ {totfinal:.2f}')
