# Classe base Veiculo, que representa veículos genéricos
class Veiculo:
    def __init__(self, marca, modelo, preco, estoque=0):
        """Inicializa um veículo com marca, modelo, preço e estoque inicial opcional"""  
        self.marca = marca
        self.modelo = modelo
        self._preco = preco
        self._estoque = estoque

    def vender(self):
        """Método para vender um veículo; reduz o estoque em 1 se houver unidades disponíveis"""
        if self._estoque > 0:
            print('Vendendo um veículo.')
            self._estoque -= 1
        else:
            print('Veículo indisponível no estoque.')

    def adicionar_estoque(self, quantidade):
        """Método para aumentar o estoque de veículos com a quantidade especificada"""
        print('Adicionando um veículo ao estoque.')
        self._estoque += quantidade
    
    @property
    def preco(self):
        """Getter para o preço do veículo, permite que ele seja acessado de forma segura"""
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        """Setter para o preço do veículo, que valida se o novo preço é positivo antes de definir"""
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            print('Não é permitido um preço abaixo de zero.')

    def exibir_informacoes(self):
        """Exibe as informações básicas do veículo: marca, modelo e preço"""
        print(f'As informações básicas do veículo são: MARCA: {self.marca}, MODELO: {self.modelo} e PRECO: {self.preco}')

    @classmethod
    def veiculo_promocional(cls, marca, modelo, preco):
        """Método de classe que cria uma instância de Veiculo com um desconto de 20% no preço original"""
        preco_com_desconto = preco * 0.8
        return cls(marca, modelo, preco_com_desconto)

# Classe Carro que herda da classe Veiculo, representando um tipo específico de veículo
class Carro(Veiculo):
    def __init__(self, marca, modelo, preco, estoque=0, numero_portas=4):
        """Inicializa um carro com a quantidade de portas e demais atributos da classe Veiculo"""
        super().__init__(marca, modelo, preco, estoque)
        self.numero_portas = numero_portas
    
    def exibir_informacoes(self):
        """Exibe as informações do carro incluindo a quantidade de portas"""
        print(f'As informações básicas do veículo são: MARCA: {self.marca}, MODELO: {self.modelo}, PRECO: {self.preco} e NUMERO DE PORTAS: {self.numero_portas}')

# Classe Caminhao que herda de Veiculo e representa um caminhão com uma capacidade de carga máxima
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, preco, carga_maxima, estoque=0):
        """Inicializa o caminhão com a carga máxima e demais atributos da classe Veiculo"""
        super().__init__(marca, modelo, preco, estoque)
        self.carga_maxima = carga_maxima

    def exibir_informacoes(self):
        """Exibe as informações do caminhão, incluindo a carga máxima suportada"""
        print(f'As informações básicas do veículo são: MARCA: {self.marca}, MODELO: {self.modelo}, PRECO: {self.preco} e CARGA MÁXIMA: {self.carga_maxima}')

# Classe LojaDeVeiculos, que representa uma loja de veículos e mantém um estoque de Veiculo
class LojaDeVeiculos:
    def __init__(self, nome):
        """Inicializa uma loja com um nome e uma lista de veículos vazia"""
        self.nome = nome
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        """Adiciona um veículo ao estoque da loja"""
        print(f'Adicionando um Veículo ao estoque da loja {self.nome}')
        self.veiculos.append(veiculo)

    def vender_veiculo(self, veiculo):
        """Vende um veículo do estoque, removendo-o da lista se o estoque atingir zero"""
        if veiculo in self.veiculos:
            veiculo.vender()
            # Remove o veículo da lista se não houver mais unidades em estoque
            if veiculo._estoque == 0:
                self.veiculos.remove(veiculo)
        else:
            print('Veiculo não encontrado no estoque.')
    
    def listar_estoque(self):
        """Lista todos os veículos em estoque na loja"""
        print(f'Estoque da loja {self.nome}')
        print()
        if self.veiculos:
            for veiculo in self.veiculos:
                print(f'{veiculo.__class__.__name__}: {veiculo.marca} {veiculo.modelo} {veiculo.preco}')
        else:
            print('Você não tem veículos para listar.')

# Instanciação de objetos e teste das funcionalidades da classe
ka = Carro('Ford', 'KA', 18000)
truck = Caminhao('Volkswagen', 'ETR12038', 200000,1000)

# Adiciona estoque aos veículos instanciados
Veiculo.adicionar_estoque(ka, 1)
Veiculo.adicionar_estoque(truck, 1)

# Cria uma loja de veículos e adiciona o carro Ford KA ao estoque da loja
loja = LojaDeVeiculos('T-CAR')
loja.adicionar_veiculo(ka)

# Exibe o estoque da loja, tenta vender o veículo duas vezes e exibe o estoque novamente
loja.listar_estoque()
loja.vender_veiculo(ka)
loja.vender_veiculo(ka)
loja.listar_estoque()

# Tenta vender o segundo veículo
loja.vender_veiculo(truck)
