from datetime import datetime
import pytz # ajuste de fuso horário


# criação da classe ContaCorrente
class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente
        cpf (str): CPF do cliente
        agencia (int): Codigo da agência responsável pela conta do cliente
        num_conta (int): Número da conta do cliente
        saldo (float): Saldo disponível na conta do cliente (alterado apenas através dos métodos da classe)
        limite (float): Limite disponível em conta para cheque especial (definido no método _limite_conta)
        transacoes (list): Histórico das transações realizadas na conta do cliente (alterado apenas através dos métodos da classe)
    """

    # método estático para armazenar informações de data e hora
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')

    # atributos de instância
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    # método consulta do saldo da conta
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:_.2f}'.format(self._saldo).replace('.', ',').replace('_', '.'))

    # método depósito de valor
    def depositar_valor(self, valor):
        self._saldo += valor
        self._transacoes.append(('Depósito: R$ {}, Novo saldo: R$ {}, Data/Hora: {}'.format(valor, self._saldo, ContaCorrente._data_hora())))

    # método privado que define o limite para cheque especial
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    # método saque de valor
    def sacar_valor(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Saldo insuficiente para realizar a transação.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append(('Saque: R$ {}, Novo saldo: R$ {}, Data/Hora: {}'.format(-valor, self._saldo, ContaCorrente._data_hora())))

    # método para consultar limite de cheque especial
    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque especial é de R$ {:_.2f}'.format(self._limite_conta()).replace('.', ',').replace('_', '.'))

    # método para consulta do histórico de transações
    def historico_transacoes(self):
        print('Histórico de transações')
        for transacao in self._transacoes:
            print(transacao)

    # método para tranferência de valores entre instâncias (contas)
    def transferir_valor(self, conta_destino, valor):
        self._saldo -= valor
        self._transacoes.append(('Transferência: R$ {}, Novo saldo: R$ {}, Data/Hora: {}'.format(-valor, self._saldo, ContaCorrente._data_hora())))
        conta_destino._saldo += valor
        conta_destino._transacoes.append(('Transferência: R$ {}, Novo saldo: R$ {}, Data/Hora: {}'.format(valor, conta_destino._saldo, ContaCorrente._data_hora())))


# programa
# criando uma instância da classe ContaCorrente e consultando saldo inicial
cc_fulano = ContaCorrente(nome='Fulano', cpf='999.888.777-66', agencia=1234, num_conta=123456)
cc_fulano.consultar_saldo()
print('-=' * 20)

# depositando valor e consultando saldo
cc_fulano.depositar_valor(10000)
cc_fulano.consultar_saldo()
print('-=' * 20)

# sacando valor e consultando saldo
cc_fulano.sacar_valor(500)
cc_fulano.consultar_saldo()
print('-=' * 20)

# tentativa de saque acima do saldo + limite
cc_fulano.sacar_valor(15000)
print('-=' * 20)

# consultar limite de cheque especial
cc_fulano.consultar_limite_chequeespecial()
print('-=' * 20)

# consultar histórico de transações
cc_fulano.historico_transacoes()
print('-=' * 20)

# transferir valor e consultar saldo da conta que enviou e da conta que recebeu
cc_ciclano = ContaCorrente(nome='Ciclano', cpf='555.444.333-22', agencia=4567, num_conta=987654)
cc_fulano.transferir_valor(cc_ciclano, 2500)
cc_fulano.consultar_saldo()
cc_ciclano.consultar_saldo()
print('-=' * 20)




