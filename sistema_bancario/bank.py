class Bank:
    def __init__(self, agency):
        """
        Inicializa a classe Bank com uma agência, uma lista de clientes e uma
        lista de contas.
        """
        self.agency = agency
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        """Adiciona um cliente à lista de clientes do banco."""
        self.customers.append(customer)  # Adiciona o cliente à lista clientes

    def add_account(self, account):
        """Adiciona uma conta à lista de contas do banco"""
        self.accounts.append(account)  # Adiciona a conta à lista de contas

    def authenticate(self, customer, account):
        """
        Autentica um cliente e uma conta verificando se pertencem ao banco e à
        agência.
        """
        # Verifica se a agência da conta corresponde à do banco
        if account.agency != self.agency:
            print('Essa conta não pertence a essa Agência')
            return False

        # Verifica se o cliente está registrado no banco
        if customer not in self.customers:
            print('Esse cliente não pertence a esse Banco')
            return False

        # Verifica se a conta está registrada no banco
        if account not in self.accounts:
            print('Essa conta não pertence a esse Banco')
            return False

        # Verifica se a conta pertence ao cliente
        if account != customer.account:
            print('Essa conta não pertence a esse Cliente')
            return False

        print('Autenticação feita com sucesso')
        return True  # Retorna True se todas as verificações foram OK


if __name__ == 'main':
    # Criando uma agência do banco
    banco = Bank('001')
