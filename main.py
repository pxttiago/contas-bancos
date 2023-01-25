from Agencias import Agencia

# programa
# criando uma instância (agência)
agencia1 = Agencia(telefone=1144556677, cnpj='11.222.333/0001-44', num_agencia=1432)

# adicionando e consultando o valor em caixa
agencia1.caixa = 10000000
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
