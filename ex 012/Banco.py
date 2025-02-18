from time import sleep

class Banco:
   def __init__(self, nome, endereco):
      self._endereço = endereco
      self._nome = nome

class Agencia(Banco):
   def __init__(self, nome, endereco, numero):
    super().__init__(nome, endereco)
    self._numero = numero
palavra = input('digiteuma palavra: ')
c = 0
while c < 100:
    c += 1
    sleep(0.1)
    print(f'{c}. {palavra.upper()}')