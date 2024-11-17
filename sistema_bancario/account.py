from abc import ABC, abstractmethod


class Account(ABC):
    """Classe Base para contas, com métodos abstratos `withdraw` e
    `deposit`."""

    def __init__(self,
                 agency: str,
                 account_number: str,
                 balance: float) -> None:
        """
        Inicializa a classe Account com os atributos de agência,
        número da conta e saldo.
        """
        self.agency: str = agency
        self.account_number: str = account_number
        self.balance: float = balance

    @abstractmethod
    def withdraw(self, amount_money: float) -> None:
        """Método abstrato para saque. Deve ser implementado
        pelas subclasses."""
        ...

    @abstractmethod
    def deposit(self, amount_money: float) -> None:
        """Método abstrato para depósito. Deve ser implementado
        pelas subclasses."""
        ...

    def details(self) -> None:
        print(f'O seu saldo é R${self.balance}')


class CurrentAccount(Account):
    """Classe de Conta Corrente que herda de Account e implementa os métodos
    abstratos conforme a necessidade de uma conta corrente,
    com limite extra."""

    def __init__(self,
                 agency: str,
                 account_number: str,
                 balance: float) -> None:
        """
        Inicializa a classe CurrentAccount, que possui um limite extra para
        saques.
        """
        super().__init__(agency, account_number, balance)
        self.extra: int = 100  # Limite extra disponível para a conta corrente

    def withdraw(self, amount_money: float) -> None:
        """
        Realiza um saque na conta corrente, considerando o saldo e o
        limite extra.

        Raises:
            ValueError: Se o valor do saque exceder o saldo disponível
            mais o limite extra.
        """
        account_balance: float = self.balance + self.extra
        if amount_money > account_balance:
            raise ValueError('Você não possui limite para saque')
        if amount_money <= 0:
            raise ValueError('Você não pode sacar 0 ou abaixo de 0')

        self.balance -= amount_money
        print(f'O valor de R${amount_money} está sendo sacado da Conta'
              'Corrente')
        self.details()

    def deposit(self, amount_money: float) -> None:
        """
        Realiza um depósito na conta corrente, somando o valor ao saldo atual.
        """
        print(f'O valor de R${amount_money} está sendo depositado na Conta'
              'Corrente')
        self.balance += amount_money  # Corrigido para +=
        self.details()


class SavingsAccount(Account):
    """Classe Conta Poupança que herda de Account e implementa os métodos
    abstratos de acordo com as necessidades de uma conta poupança."""

    def withdraw(self, amount_money: float) -> None:
        """
        Realiza um saque na conta poupança, subtraindo o valor do saldo
        disponível.

        Raises:
            ValueError: Se o valor do saque exceder o saldo disponível.
        """
        if amount_money > self.balance:
            raise ValueError('Você não possui limite para saque')
        if amount_money <= 0:
            raise ValueError('Você não pode sacar 0 ou abaixo de 0')

        self.balance -= amount_money  # Corrigido para -=
        print(f'O valor de R${amount_money} está sendo sacado da Conta'
              'Poupança')
        self.details()

    def deposit(self, amount_money: float) -> None:
        """
        Realiza um depósito na conta poupança, somando o valor ao saldo atual.
        """
        print(f'O valor de R${amount_money} está sendo depositado na Conta'
              'Poupança')
        self.balance += amount_money  # Corrigido para +=
        self.details()


# criando contas
contacorrente = CurrentAccount('001', '12345-6', 500)
contapoupanca = SavingsAccount('002', '67890-1', 300)
