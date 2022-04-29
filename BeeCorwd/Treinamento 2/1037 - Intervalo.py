num = float(input())
intervalo = ['Intervalo [0,25]', 'Intervalo (25,50]', 'Intervalo (50,75]', 'Intervalo (75,100]', 'Fora de intervalo']
if num > 0 and num <= 25:
    print(intervalo[0])
elif num > 25 and num <= 50:
    print(intervalo[1])
elif num > 50 and num <= 75:
    print(intervalo[2])
elif num > 75 and num <= 100:
    print(intervalo[3])
else:
    num < 0 and num > 100
    print(intervalo[4])
