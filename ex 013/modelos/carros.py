from modelos.veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, porta):
        self.porta = porta
        super().__init__(marca, modelo, ano)
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} - Porta: {self.porta} - Status: {status}"