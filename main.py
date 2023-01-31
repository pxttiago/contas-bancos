from Agencias import Agencia, AgenciaVirtual, AgenciaComum, AgenciaPremium

# programa
# criando uma instância (agência)
agencia1 = Agencia(telefone=1144556677, cnpj='11.222.333/0001-44', num_agencia=1432)

# adicionando e consultando o valor em caixa
agencia1.caixa = 1000000
agencia1.verificar_caixa()
print('-=' * 20)

# adicionando cliente
agencia1.adicionar_cliente(nome='Fulano', cpf='999.888.777-66', patrimonio=15000)
print(agencia1.clientes)
print('-=' * 20)

# realizando empréstimo
agencia1.emprestar_dinheiro(valor=10000, cpf='999.888.777-66', juros=0.02)
agencia1.verificar_caixa()
print('-=' * 20)

# criando um objeto AgenciaVirtual e consultando o valor de caixa
agencia_virtual = AgenciaVirtual(site='www.agenciavirtual.com.br', telefone=2233334444, cnpj='88.777.666/0001-55')
agencia_virtual.verificar_caixa()
print('-=' * 20)

# criando um objeto AgenciaComum e consultando o número da agência
agencia_comum = AgenciaComum(telefone=3355556666, cnpj='77.333.555/0001-66')
print(agencia_comum.num_agencia)
print('-=' * 20)

# criando um objeto AgenciaPremium e consultando o valor de caixa
agencia_premium = AgenciaPremium(telefone=9988886666, cnpj='11333555/0001-77')
agencia_premium.verificar_caixa()
print('-=' * 20)

# depositando valor da AgendiaVirtual no caixa paypal
agencia_virtual.depositar_paypal(valor=50000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)
print('-=' * 20)

# tentando adicionar cliente abaixo do patrimônio mínimo na agência premium
agencia_premium.adicionar_cliente('Beltrano', '999.666.333-11', 500000)