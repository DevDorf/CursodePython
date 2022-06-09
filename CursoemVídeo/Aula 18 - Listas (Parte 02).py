'''teste = []
galera = []
teste.append('Caio')
teste.append(40)
galera.append(teste[:]) #quando colocamos somento o nome da variavel, criamos uma ligação, para criar a copia tem que colocar o simbolo para varer a lista.
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) #O primeiro numero chaca o indice dentro de galera e o segundo chama o indice dentro do indice do primeiro numero
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')'''

galera = []
dado = []
totmai = totmen = 0
for p in range(0, 3):
    dado.append(input('Nome: '))
    dado.append((int(input('Idade: ')))) #Estrutura que ler e armazena os dados dentro da lista
    galera.append(dado[:])
    dado.clear()

for p in galera: #Verifica de o valor de idade é maior ou menor de idade
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print((f'{p[0]} é menor de idade'))
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
