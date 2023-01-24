# criação da classe ContaCorrente
class ContaCorrente:

    # atributos
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    # método consulta do saldo da conta
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:_.2f}'.format(self.saldo).replace('.', ',').replace('_', '.'))

    # método depósito de valor
    def depositar_valor(self, valor):
        self.saldo += valor

    # método saque de valor
    def sacar_valor(self, valor):
        self.saldo -= valor


# programa
# criando uma instância da classe ContaCorrente e consultando saldo inicial
cc_fulano = ContaCorrente(nome='Fulano', cpf='999.888.777-66')
cc_fulano.consultar_saldo()
print('-=' * 20)

# depositando valor e consultando saldo
cc_fulano.depositar_valor(10000)
cc_fulano.consultar_saldo()
print('-=' * 20)

# sacando valor e consultando saldo
cc_fulano.sacar_valor(500)
cc_fulano.consultar_saldo()






