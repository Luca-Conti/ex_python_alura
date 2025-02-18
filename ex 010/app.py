import os
class ContaBancaria():
    contas = []
    def __init__(self, titular, saldo, email, senha):
        self._titular = titular
        self._saldo = saldo
        self.email = email
        self.senha = senha
        self._ativar = True
        ContaBancaria.contas.append(self)
    def __str__(self):
        return f'{self._titular} || {self._saldo}'

    
    @classmethod
    def listar(cls):
        print(f'{'Titular'.ljust(25)} || {'Saldo'}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(25)} || {conta._saldo}')
def exibir_texto(texto):
    os.system('cls')
    print('-' * (len(texto)
     + 1))
    print(texto)
    print('-' * (len(texto) + 1))
    print()

def voltar_pro_menu():
    input('Digite algo para voltar pro menu: ')
    os.system('cls')
    main()

def titulo():
    print('''
██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ██╗░░░░░██╗░░░██╗░█████╗░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██║░░░░░██║░░░██║██╔══██╗██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ██║░░░░░██║░░░██║██║░░╚═╝███████║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██║░░░░░██║░░░██║██║░░██╗██╔══██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ███████╗╚██████╔╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ╚══════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝
''')

def cadastra_conta():
    exibir_texto(texto='Cadastra Conta')
    nome = input('qual é o do titular da conta: ').title()
    saldo = float(input('qual é o saldo da sua conta: '))
    email = input('Digite o um email para cadastra não sua conta: ')
    senha = input('Digite uma senha com no minimo 8 digitos: ')
    confirmacao_de_senha = input('Confirme a senha: ')
    senha_numero = 'aaaaaaaa'
    if senha == confirmacao_de_senha and len(senha) >= len(senha_numero):
        conta = ContaBancaria(nome, saldo, email, senha)
        voltar_pro_menu()
    else:
        print('Faça o cadastro de novo')
        input('Digite algo para voltar pro cadastro')
        cadastra_conta()

def listar_conta():
    exibir_texto(texto='Lista Contas')
    ContaBancaria.listar()
    voltar_pro_menu()

def opicao():
    try:
        print('''OPIÇÃO
        
        1. Cadastra Conta
        2. Listar Conta
        3. Sair''')
        opicao_escolida = int(input('Escolha uma opiçaõ: '))
    
        if opicao_escolida == 1:
            cadastra_conta()
        elif opicao_escolida == 2:
            listar_conta()
        elif opicao_escolida == 3:
            finalizar_app()
        else:
            opicao_errada()
    except:
        opicao_errada()
    

def finalizar_app():
    exibir_texto(texto='Finalizar o APP')

def opicao_errada():
    exibir_texto(texto='Opição Errada')
    input('Digite algo para voltar pro menu')
    main()

def main():
    titulo()
    opicao()
main()



