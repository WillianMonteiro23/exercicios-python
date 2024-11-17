from bank import Bank
from people import Customer
from account import CurrentAccount, SavingsAccount

# Criando uma agência do banco
banco = Bank('001')

# Criando contas
contacorrente = CurrentAccount('001', '12345-6', 500)
contapoupanca = SavingsAccount('002', '67890-1', 300)

# Criando clientes
cliente1 = Customer('João Silva', 30, contacorrente)
cliente2 = Customer("Maria Oliveira", 28, contapoupanca)

# Adicionando clientes e contas ao banco
banco.add_customer(cliente1)
banco.add_customer(cliente2)
banco.add_account(cliente1.account)
banco.add_account(cliente2.account)

# Testando a autenticação e saque para o cliente1
if banco.authenticate(cliente2, cliente2.account):
    cliente2.account.withdraw(100)

if banco.authenticate(cliente1, cliente1.account):
    cliente1.account.withdraw(100)

if banco.authenticate(cliente1, cliente1.account):
    cliente1.account.withdraw(0)
