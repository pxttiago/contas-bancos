from datetime import datetime
import pytz # ajuste de fuso horário


# criação da classe ContaCorrente
class ContaCorrente:

    # método estático para armazenar informações de data e hora
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')

    # atributos
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    # método consulta do saldo da conta
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:_.2f}'.format(self.saldo).replace('.', ',').replace('_', '.'))

    # método depósito de valor
    def depositar_valor(self, valor):
        self.saldo += valor
        self.transacoes.append(('Depósito: R$ {}, Novo saldo: R$ {}, Data/Hora: {}'.format(valor, self.saldo, ContaCorrente._data_hora())))

    # método privado que define o limite para cheque especial
    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    # método saque de valor
    def sacar_valor(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Saldo insuficiente para realizar a transação.')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append(('Saque: R$ {}, Novo saldo: R$ {}, Data/Hora: {}'.format(-valor, self.saldo, ContaCorrente._data_hora())))

    # método para consultar limite de cheque especial
    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque especial é de R$ {:_.2f}'.format(self._limite_conta()).replace('.', ',').replace('_', '.'))

    def historico_transacoes(self):
        print('Histórico de transações')
        for transacao in self.transacoes:
            print(transacao)


# programa
# criando uma instância da classe ContaCorrente e consultando saldo inicial
cc_fulano = ContaCorrente(nome='Fulano', cpf='999.888.777-66', agencia='0123', num_conta='123456')
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





