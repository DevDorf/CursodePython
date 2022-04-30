palavra1 = str(input())
palavra2 = str(input())
palavra3 = str(input())

palavras = [palavra1, palavra2, palavra3]

if palavras[0] == 'vertebrado' and palavras[1] == 'ave' and palavras[2] == 'carnivoro':
    print('aguia')
elif palavras[0] == 'vertebrado' and palavras[1] == 'ave' and palavras[2] == 'onivoro':
    print('pomba')
elif palavras[0] == 'vertebrado' and palavras[1] == 'mamifero' and palavras[2] == 'onivoro':
    print('homem')
elif palavras[0] == 'vertebrado' and palavras[1] == 'mamifero' and palavras[2] == 'herbivoro':
    print('vaca')
elif palavras[0] == 'invertebrado' and palavras[1] == 'inseto' and palavras[2] == 'hematofago':
    print('pulga')
elif palavras[0] == 'invertebrado' and palavras[1] == 'inseto' and palavras[2] == 'herbivoro':
    print('lagarta')
elif palavras[0] == 'invertebrado' and palavras[1] == 'anelideo' and palavras[2] == 'hematofago':
    print('sanguessuga')
else:
    print('minhoca')



