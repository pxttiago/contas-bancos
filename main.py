from ContasBancos import ContaCorrente, CartaoCredito

# programa
# criando uma instância da classe ContaCorrente
cc_fulano = ContaCorrente(nome='Fulano', cpf='999.888.777-66', agencia=1234, num_conta=123456)

# criando uma instância da classe CartaoCredito
cartao_fulano = CartaoCredito(titular='Fulano', conta_corrente=cc_fulano)

# verificando os dados do cartão
print(cartao_fulano.__dict__)
print('-=' * 20)
