class Teste:
    def __init__(self):
        self.__nome = 0
        self.cont = 0

    @property
    def nome(self):
        print('Executando a propety...')
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        print('Executando o setter...')
        self.__nome = novo_nome

t1 = Teste()



