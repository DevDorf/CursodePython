num = int(input())
if num % 2 == 0:
    anterior = num - 1
    posterior = num + 2
else:
    anterior = num - 2
    posterior = num + 1
print('{} {}'.format(anterior, posterior))
