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
