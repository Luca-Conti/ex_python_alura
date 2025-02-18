class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self):
        print(self.modelo, self.cor, self.ano)


toyata = Carro('rav4', 'preto', 2020)
Carro.__str__

class restauraetes():
    def __init__(self):
        pass