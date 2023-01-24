from ContasBancos import ContaCorrente

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