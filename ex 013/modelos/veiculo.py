from colorama import Fore, Style
from time import sleep

class Veiculo:
    veiculos = []
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._ligado = False
        self.veiculos = Veiculo.veiculos
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"{self.marca} {self.modelo} - Status: {status}"

