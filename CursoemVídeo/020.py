# quer que leia 4 alunos novamente e sorteia o nome e mostre a ordem
from random import shuffle
n1 = str(input('Digite nome 1: '))
n2 = str(input('Digite nome 2: '))
n3 = str(input('Digite nome 3: '))
n4 = str(input('Digite nome 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem para apresentação dos alunos é {}'.format(lista))


