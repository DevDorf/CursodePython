n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
par = 0
if n1 % 2 == 0:
    par = par + 1
if n2 % 2 == 0:
    par = par + 1
if n3 % 2 == 0:
    par = par + 1
if n4 % 2 == 0:
    par = par +1
if n5 % 2 == 0:
    par = par +1
print('{} valores pares'.format(par))
