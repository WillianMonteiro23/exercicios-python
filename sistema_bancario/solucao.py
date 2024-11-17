from bank import Bank
from people import Customer
from account import CurrentAccount, SavingsAccount

"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

Criar um sistema bancário que tem clientes, contas e um banco. A ideia é que o 
cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar
nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

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
