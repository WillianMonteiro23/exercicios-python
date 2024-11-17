from account import contacorrente, contapoupanca, Account


class People:

    def __init__(self, name: str, age: int):
        """Inicializa a classe People com atributos nome e idade"""
        self._name = name  # Atribui o nome ao atributo privado _name
        self._age = age    # Atribui a idade ao atributo privado _age

    @property
    def name(self) -> str:
        """Getter para o atributo name"""
        return self._name

    @property
    def age(self) -> int:
        """Getter para o atributo age."""
        return self._age


class Customer(People):
    def __init__(self, name: str, age: int, account: Account):
        """
        Inicializa a classe Customer, que herda de People e associa uma conta
        bancária ao cliente.
        """
        super().__init__(name, age)  # Inicializa herdando da classe People
        self.account = account  # Associa uma conta bancária ao cliente


if __name__ == 'main':
    # Criando clientes e contas
    cliente1 = Customer('João Silva', 30, contacorrente)
    cliente2 = Customer("Maria Oliveira", 28, contapoupanca)
