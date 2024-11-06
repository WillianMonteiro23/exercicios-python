# Classe base Veiculo, que representa veículos genéricos
class Vehicle:
    def __init__(self, brand, model, price, stock=0):
        """Inicializa um veículo com marca, modelo, preço e estoque inicial opcional"""  
        self.brand = brand
        self.model = model
        self._price = price
        self._stock = stock

    def sell(self):
        """Método para vender um veículo; reduz o estoque em 1 se houver unidades disponíveis"""
        if self._stock > 0:
            print('Vendendo um veículo.')
            self._stock -= 1
        else:
            print('Veículo indisponível no estoque.')

    def add_stock(self, quantity):
        """Método para aumentar o estoque de veículos com a quantidade especificada"""
        print('Adicionando um veículo ao estoque.')
        self._stock += quantity
    
    @property
    def price(self):
        """Getter para o preço do veículo, permite que ele seja acessado de forma segura"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Setter para o preço do veículo, que valida se o novo preço é positivo antes de definir"""
        if new_price > 0:
            self._price = new_price
        else:
            print('Não é permitido um preço abaixo de zero.')

    def display_info(self):
        """Exibe as informações básicas do veículo: marca, modelo e preço"""
        print(f'As informações básicas do veículo são: MARCA: {self.brand}, MODELO: {self.model} e PRECO: {self.price}')

    @classmethod
    def promotional_vehicle(cls, brand, model, price):
        """Método de classe que cria uma instância de Vehicle com um desconto de 20% no preço original"""
        discounted_price = price * 0.8
        return cls(brand, model, discounted_price)

# Classe Carro que herda da classe Vehicle, representando um tipo específico de veículo
class Car(Vehicle):
    def __init__(self, brand, model, price, stock=0, number_of_doors=4):
        """Inicializa um carro com a quantidade de portas e demais atributos da classe Vehicle"""
        super().__init__(brand, model, price, stock)
        self.number_of_doors = number_of_doors
    
    def display_info(self):
        """Exibe as informações do carro incluindo a quantidade de portas"""
        print(f'As informações básicas do veículo são: MARCA: {self.brand}, MODELO: {self.model}, PRECO: {self.price} e NUMERO DE PORTAS: {self.number_of_doors}')

# Classe Caminhao que herda de Vehicle e representa um caminhão com uma capacidade de carga máxima
class Truck(Vehicle):
    def __init__(self, brand, model, price, max_load, stock=0):
        """Inicializa o caminhão com a carga máxima e demais atributos da classe Vehicle"""
        super().__init__(brand, model, price, stock)
        self.max_load = max_load

    def display_info(self):
        """Exibe as informações do caminhão, incluindo a carga máxima suportada"""
        print(f'As informações básicas do veículo são: MARCA: {self.brand}, MODELO: {self.model}, PRECO: {self.price} e CARGA MÁXIMA: {self.max_load}')

# Classe LojaDeVeiculos, que representa uma loja de veículos e mantém um estoque de Vehicle
class VehicleStore:
    def __init__(self, name):
        """Inicializa uma loja com um nome e uma lista de veículos vazia"""
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Adiciona um veículo ao estoque da loja"""
        print(f'Adicionando um Veículo ao estoque da loja {self.name}')
        self.vehicles.append(vehicle)

    def sell_vehicle(self, vehicle):
        """Vende um veículo do estoque, removendo-o da lista se o estoque atingir zero"""
        if vehicle in self.vehicles:
            vehicle.sell()
            # Remove o veículo da lista se não houver mais unidades em estoque
            if vehicle._stock == 0:
                self.vehicles.remove(vehicle)
        else:
            print('Veículo não encontrado no estoque.')
    
    def list_stock(self):
        """Lista todos os veículos em estoque na loja"""
        print(f'Estoque da loja {self.name}')
        print()
        if self.vehicles:
            for vehicle in self.vehicles:
                print(f'{vehicle.__class__.__name__}: {vehicle.brand} {vehicle.model} {vehicle.price}')
        else:
            print('Você não tem veículos para listar.')

# Instanciação de objetos e teste das funcionalidades da classe
ka = Car('Ford', 'KA', 18000)
truck = Truck('Volkswagen', 'ETR12038', 200000, 1000)

# Adiciona estoque aos veículos instanciados
Vehicle.add_stock(ka, 1)
Vehicle.add_stock(truck, 1)

# Cria uma loja de veículos e adiciona o carro Ford KA ao estoque da loja
store = VehicleStore('T-CAR')
store.add_vehicle(ka)

# Exibe o estoque da loja, tenta vender o veículo duas vezes e exibe o estoque novamente
store.list_stock()
store.sell_vehicle(ka)
store.sell_vehicle(ka)
store.list_stock()

# Tenta vender o segundo veículo
store.sell_vehicle(truck)
