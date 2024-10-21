"""
Exercício: Sistema de Gerenciamento de Biblioteca

Você deve criar um sistema simples para gerenciar livros em uma biblioteca. 
O sistema deve ser capaz de adicionar livros, listar livros disponíveis e manter 
um contador de quantos livros foram adicionados.

 O sistema deve permitir:

    - Adicionar livros à biblioteca com informações como título, autor e 
    disponibilidade para empréstimo.

    - Manter um controle da quantidade total de livros que foram adicionados à 
    biblioteca.

    - Emprestar e devolver livros, alterando seu status de disponibilidade.

    - Exibir a disponibilidade de cada livro com uma mensagem apropriada.

    - Armazenar e listar todos os livros disponíveis na biblioteca, junto com suas 
    informações e status de disponibilidade.

    - Retornar o total de livros adicionados ao sistema de forma global.
"""

# criando classe Livros
class Livro:
    contador_livros = 0 # contador de quantos livros foram adicionados

    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo # atributo de instância
        self.autor = autor
        self.disponivel = disponivel
        Livro.contador_livros += 1 # incrmenta o contador

    @classmethod
    def adicionar_livro(cls, titulo, autor):
        """Método de classe para adicionar um livro"""
        novo_livro = cls(titulo, autor)
        return novo_livro

    def emprestar(self):
        """Método de instância para emprestar um livro"""
        if not self.disponivel:
            print(f'O livro {self.titulo} não está disponível!') # caso o livro já esteja emprestado
            return 
        print(f'Emprestando livro {self.titulo}')
        self.disponivel = False # caso o livro esteja disponivel atualizamos para deixar indisponivel

    def devolver(self):
        """Método de instância que devolve o livro"""
        print(f'Devolvendo o livro {self.titulo}')
        self.disponivel = True # o livro que antes estava emprestado(False), agora atualizamos para disponivel
        
    @property
    def disponibilidade(self):
        """Getter que retorna a disponibilidade do livro"""
        if self.disponivel:
            return 'Disponível'
        return 'Indisponível'

# criando classe Biblioteca
class Biblioteca:
    livros = [] # atributo de classe que receberá os livros adcionados

    @classmethod
    def adicionar_livro(cls, titulo, autor):
        """Método de classe que adiciona um novo livro utilizando como base o método de classe de Livro"""
        novo_livro = Livro.adicionar_livro(titulo, autor) 
        cls.livros.append(novo_livro)
        return novo_livro
    
    @classmethod
    def listar_livros(cls):
        """Método de classe que lista todos os livros existentes na biblioteca"""
        for livro in cls.livros:
            print(f'LIVRO: {livro.titulo}, AUTOR: {livro.autor}, DISPONIBILIDADE: {livro.disponibilidade}')
    
    @classmethod
    def total_livros(cls):
        """Método de classe que retorna a quantidade de livros que foram adicionados"""
        return Livro.contador_livros

# Testando o sistema
if __name__ == "__main__":
    # Adicionando livros à biblioteca
    Biblioteca.adicionar_livro('Python vol1','Autor 1')
    Biblioteca.adicionar_livro('Python vol2','Autor 2')
    Biblioteca.adicionar_livro('Python vol3','Autor 3')
    Biblioteca.adicionar_livro('Python vol3','Autor 4')
    Biblioteca.adicionar_livro('Python vol3','Autor 5')
    Biblioteca.adicionar_livro('Python vol3','Autor 6')

# total de livros adicionador - 6
print('Total livros:')
print(Biblioteca.total_livros()) 
print()

# listando livro a livro que foram adicionados
print('Livros presentes na Biblioteca:')
Biblioteca.listar_livros() 
print()

# atribuindo o primeiro livro da biblioteca a uma variavel
livro = Biblioteca.livros[0] 

# acessando atributo titulo
print(livro.titulo) 

# acessando atributo autor
print(livro.autor)

# acessando atributo(getter) titulo
print(livro.disponibilidade)

# emprestando livro
livro.emprestar() 

# a disponibilidade antes True agora se tornou False, já que emprestamos o livro
print(livro.disponibilidade) 

# se tentarmos emprestar de novo, aparece que esse livro não esta disponivel
livro.emprestar() 

# devolvendo, atualizamos o atributo disponivel para True
livro.devolver() 

print(livro.disponibilidade)
