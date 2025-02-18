class Livro:
    def __init__(self, titulo, autor, ano_de_lancamento):
        self._titulo = titulo
        self._autor = autor
        self._ano_de_laancamento = ano_de_lancamento
        self._disponivel = True
    
    def __str__(self):
        return f'o titulo {self.titulo} autor {self.autor} ano de lncamneto {self.ano_de_laancamento}'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @classmethod
    def verificar_disponibilidade(cls, ano):
        



livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")
    
livro1 = Livro('JK.ROULING', 'harry potter', 2012)
print(vars(livro1))
Livro.emprestar()