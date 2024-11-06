
"""
Imagine que você está desenvolvendo um sistema que permite que apenas usuários 
autenticados com uma função específica (ex.: "admin") executem determinadas 
operações críticas.

Objetivo: Criar uma classe Usuario com decoradores para gerenciar autenticação 
e autorização de acesso.
"""

def check_authentication(method):
    """Funcao decoradora que contem a logica de permissao das autenticações"""
    def wrapper(self, *args, **kwargs):
        print('Verificando permissao')
        if self.authentication:
            return method(self, *args, **kwargs)
        raise PermissionError('Você não está autenticado para acessar os dados.')
    return wrapper

def check_permission(method):
    """Funcao decoradora que contem a logica de permissao para executar operaçoes criticas"""
    def wrapper(self, *args, **kwargs):
        if self.func != 'admin':
            raise PermissionError('Permissao negada: Somente admins podem fazer operações criticas')
        return method(self, *args, **kwargs)
    return wrapper

class User:
    """Criando uma classe para criar Usuarios"""
    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.authentication = False
    
    def authenticate(self):
        """Funcao que autentica um User"""
        self.authentication = True
        print(f'O usuario {self.name} foi autenticado')

    @check_authentication
    def access_data(self):
        """Funcao decorada que da acesso a dados"""
        print(f'Acesso permitido aos dados ao user {self.name}')
    
    @check_permission
    @check_authentication
    def perform_critical_operation(self):
        """Funcao decorada que executa operaçoes criticas"""
        print(f'Acesso permitido ao user {self.name} para fazer operações criticas')

# testando código
maria = User('Maria', 'admin')
joao = User('Joao', 'comum')
maria.authenticate() # autenticando user Maria
maria.access_data() # podemos acessar os dados pois estamos autenticados
maria.perform_critical_operation() # como Maria tem autenticaçao + admin, pode fazer operaçoes criticas
joao.access_data() # levanta uma exceçao, ja que nao estamos autenticados
joao.authenticate()  # autenticando user Joao
joao.access_data() # acessando dados
joao.perform_critical_operation() # o usuario Joao nao tem permissao de admin para fazer operacoes criticas

