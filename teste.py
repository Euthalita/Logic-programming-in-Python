class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(nome, idade)

    def comer(self, cumeu):
        if cumeu == 'YES':
            print(f'{self.nome} esta comendo')
        else:
            print(f'{self.nome} não esta comendo')


p1 = Pessoa('Carla', 23)
a = input(f'{p1.nome} está comendo?').upper()
p1.comer(a)











