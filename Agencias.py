from random import randint


class Agencia:

    """
    Cria um objeto Agência para gerênciar as agências da rede bancária

    Atributos:
        telefone (int): Telefone da agência
        cnpj (str): CNPJ da agência
        num_agencia (int): Código da agência
        clientes (list): Lista com as informações dos clientes da agência
        caixa (float): Valor em caixa disponível na agência
        emprestimos (list): Lista com informações sobre os empréstimos realizados pela agência
    """

    # atributos de instância
    def __init__(self, telefone, cnpj, num_agencia):
        self.telefone = telefone
        self.cnpj = cnpj
        self.num_agencia = num_agencia
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    # método que verifica o valor de caixa disponível na agência
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual R$ {:_.2f}'.format(self.caixa).replace('.', ',').replace('_', '.'))
        else:
            print('O valor de caixa está OK. Caixa atual R$ {:_.2f}'.format(self.caixa).replace('.', ',').replace('_', '.'))

    # método que gerencia os empréstimos que a agencia realizou
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            self.caixa -= valor
        else:
            print('Empréstimo indisponível. Valor insuficiente em caixa.')

    # método para cadastro dos clientes da agência
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# criação da subclasse AgenciaVirtual herdando as características da classe Agencia
class AgenciaVirtual(Agencia):

    # atributos da subclasse AgenciaVirtual
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    # métodos específicos da subclasse AgenciaVirtual
    def depositar_paypal(self, valor):
        if valor < self.caixa:
            self.caixa -= valor
            self.caixa_paypal += valor
        else:
            print('Saldo insuficiente em caixa na agência.')

    def sacar_paypal(self, valor):
        if valor < self.caixa_paypal:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print('Saldo insuficiente em caixa no paypal.')


# criação da subclasse AgenciaComum herdando as características da classe Agencia
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, num_agencia=randint(1001, 9999))
        self.caixa = 1000000


# criação da subclasse AgenciaPremium herdando as características da classe Agencia
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, num_agencia=randint(1001, 9999))
        self.caixa = 100000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não possui o patrimônio mínimo exigido para entrar na Agência Premium.')