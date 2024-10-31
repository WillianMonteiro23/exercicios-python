# Repositório de Exercícios de Python

Bem-vindo ao repositório de **Exercícios de Python**! Este espaço foi criado para ajudar no desenvolvimento e aperfeiçoamento de suas habilidades em programação Python, com uma variedade de desafios práticos, desde conceitos básicos até tópicos mais avançados.

### 📚 O que será desenvolvido?

Ao longo deste repositório, você encontrará exercícios que abordarão:

- **Conceitos fundamentais**: estruturas de controle, laços, condicionais e funções.
- **Manipulação de dados**: listas, dicionários, tuplas e conjuntos.
- **Algoritmos e lógica de programação**: resolução de problemas práticos e desafios lógicos.
- **Orientação a objetos**: classes, herança e polimorfismo.
- **Manipulação de arquivos**: leitura e escrita de arquivos.
- **Integração com bibliotecas externas**: uso de bibliotecas populares para expandir funcionalidades.

Cada exercício será acompanhado de uma explicação sobre o problema e um esboço do que precisa ser desenvolvido, proporcionando a você uma experiência prática focada no aprendizado incremental.

### 📑 Índice

- [Algoritmo de Validação do CPF](#algoritmo-de-validação-do-cpf)
- [Gerenciador de Tarefas](#gerenciador-de-tarefas)
- [Jogo de Adivinhação da Palavra Secreta](#jogo-de-adivinhação-da-palavra-secreta)
- [Sistema de Perguntas e Respostas](#sistema-de-perguntas-e-respostas)
- [Sistema de Gerenciamento de Biblioteca](#sistema-de-gerenciamento-de-biblioteca)
- [Verificador de Numero Primo](#verificador-de-numero-primo)
- [Sistema de Gestão de Veículos](#sistema-de-gestao-de-veiculos)


### 🎯 Como isso pode auxiliar nos estudos?

Os exercícios propostos aqui foram desenvolvidos com o objetivo de fortalecer sua base em Python e lógica de programação. Ao trabalhar nos problemas, você:

- **Solidifica a compreensão** dos conceitos teóricos aprendidos em aulas e tutoriais.
- **Desenvolve a habilidade de resolver problemas** do mundo real, ganhando confiança na escrita de código limpo e eficiente.
- **Pratica a lógica e raciocínio**, o que é essencial para entrevistas de emprego e desafios técnicos.

Além disso, muitos exercícios incluem sugestões de reflexão, levando você a pensar em diferentes formas de abordar a mesma solução.

### ⚠️ Quão desafiadores são os exercícios?

Os exercícios são progressivos em dificuldade. Aqui está uma visão geral:

- **Iniciantes**: exercícios que focam na sintaxe e lógica básica, como loops e condicionais.
- **Intermediários**: problemas que introduzem estruturas de dados, funções, e manipulação de dados em maior escala.
- **Avançados**: exercícios mais complexos, envolvendo conceitos de programação orientada a objetos, otimização de algoritmos e desafios de integração com bibliotecas externas.

Sinta-se à vontade para avançar no seu próprio ritmo. Cada exercício é projetado para desafiá-lo, mas também para ser realizável com prática e paciência.

### 💡 Dicas para resolver os exercícios

- **Divida o problema em partes menores**: Muitas vezes, dividir um problema complexo em subtarefas mais simples ajuda a encontrar uma solução mais clara.
- **Teste frequentemente**: Não espere para testar seu código no final. Execute pequenas partes conforme vai construindo a solução.
- **Faça uso da documentação**: A documentação oficial do Python é uma excelente fonte de referência. Não hesite em consultá-la quando tiver dúvidas.
- **Não se preocupe em falhar**: O processo de aprendizado envolve tentativa e erro. Cada erro é uma oportunidade de entender melhor o problema e aprender algo novo.
- **Procure soluções alternativas**: Após resolver um problema, tente abordá-lo de outra maneira. Isso ajuda a expandir suas habilidades e melhora sua adaptabilidade em diferentes situações.

### 📑 Boas práticas de estudo

- **Dedicação e consistência**: Estudar e praticar regularmente é fundamental. Estabeleça uma rotina de prática diária ou semanal.
- **Escreva um código limpo**: Organize seu código de forma que seja legível e bem documentado. Use nomes de variáveis significativos e adicione comentários sempre que necessário.
- **Colabore com outros**: Se possível, compartilhe suas soluções com colegas ou participe de comunidades online. A troca de ideias pode fornecer novos insights.
- **Revisite exercícios antigos**: À medida que avança, volte para os exercícios que você já fez e tente resolvê-los de formas diferentes, ou usando técnicas que aprendeu recentemente.

## Algoritmo de Validação do CPF
### Exercício Proposto: Criar um Validador de CPF

### Descrição

O Cadastro de Pessoas Físicas (CPF) é um documento essencial para a identificação de cidadãos brasileiros. Neste exercício, você será desafiado a implementar um programa que valide a integridade de um CPF com base em um algoritmo específico. 

### Objetivo

O objetivo deste exercício é criar uma função que receba um CPF como entrada, verifique se ele é válido e retorne um resultado indicando a validade do CPF.

### Lógica do Algoritmo

A lógica do algoritmo é baseada em um método de verificação que utiliza os 9 primeiros dígitos do CPF para calcular os dois dígitos verificadores. A ideia é que a sequência de operações matemáticas aplicadas aos dígitos de um CPF válido produza resultados que sempre respeitarão um padrão específico. Esses cálculos não são aleatórios, mas seguem uma regra lógica que permite validar o CPF.

### Requisitos

1. **Entrada de Dados**:
   - O usuário deve inserir o CPF sem formatação (apenas números), garantindo que ele contenha 11 dígitos.

2. **Validação**:
   - Verifique se o CPF contém 11 dígitos. Caso contrário, retorne uma mensagem informando que o CPF é inválido.
   - Certifique-se de que o CPF não é composto por números repetidos (exemplo: 111.111.111-11 é inválido).

3. **Cálculo dos Dígitos Verificadores**:
   - Implemente a lógica para calcular os dois dígitos verificadores do CPF:
     - **Primeiro dígito**:
       - Multiplique os 9 primeiros dígitos por pesos que vão de 10 a 2 e some os resultados.
       - Multiplique a soma por 10 e calcule o resto da divisão por 11. O resultado deve ser o primeiro dígito verificador (se o resultado for 10 ou maior, o dígito é 0).
     - **Segundo dígito**:
       - Multiplique os 9 primeiros dígitos e o primeiro dígito verificador por pesos que vão de 11 a 2 e some os resultados.
       - Multiplique a soma por 10 e calcule o resto da divisão por 11. O resultado deve ser o segundo dígito verificador (se o resultado for 10 ou maior, o dígito é 0).

4. **Saída**:
   - Compare os dígitos verificadores calculados com os fornecidos pelo usuário. Informe se o CPF é válido ou inválido.

### Dicas

- Utilize listas para armazenar os dígitos do CPF e realizar as operações necessárias.
- Teste sua função com diferentes entradas, incluindo CPFs válidos e inválidos, para garantir que a lógica está correta.

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/algoritmo-validacao-cpf/solucao.py) ⬅️ 


## Gerenciador de Tarefas

### Descrição

Neste exercício, você irá desenvolver um gerenciador de tarefas simples em Python. O programa deve permitir que o usuário crie uma lista de tarefas, além de oferecer funcionalidades para gerenciar essas tarefas de forma eficiente.

### Objetivo

O objetivo é implementar um programa que permita ao usuário adicionar tarefas à lista e gerenciá-las através de diversas operações.

### Lógica do Algoritmo

A lógica do algoritmo é baseada em um método de verificação que utiliza os 9 primeiros dígitos do CPF para calcular os dois dígitos verificadores. A ideia é que a sequência de operações matemáticas aplicadas aos dígitos de um CPF válido produza resultados que sempre respeitarão um padrão específico. Esses cálculos não são aleatórios, mas seguem uma regra lógica que permite validar o CPF.

### Requisitos

1. **Adicionar Tarefas**:
   - O usuário pode digitar qualquer tarefa e essa tarefa deve ser adicionada a uma lista de tarefas.

2. **Funcionalidades**:
   - O programa deve oferecer as seguintes opções:
     - **Listar as Tarefas**: Exibir todas as tarefas atualmente na lista.
     - **Desfazer a Última Tarefa**: Remover a tarefa que foi adicionada mais recentemente e armazená-la em uma lista de tarefas desfeitas.
     - **Refazer a Tarefa Desfeita**: Restaurar a última tarefa que foi desfeita.
     - **Limpar a Tela**: Limpar a tela do console, mas manter a lista de tarefas inalterada.
     - **Salvar a Lista**: Salvar o estado atual da lista de tarefas em um arquivo para que possa ser recarregada posteriormente.
     - **Parar a Listagem de Tarefas**: Encerrar o programa e salvar o estado atual da lista de tarefas.

3. **Persistência de Dados**:
   - As tarefas devem ser salvas em um arquivo (por exemplo, em formato de texto) quando o usuário optar por salvar ou parar a listagem. Ao reiniciar o programa, as tarefas salvas devem ser carregadas automaticamente.

### Dicas

- **Estruture seu Código**: Considere dividir seu programa em funções distintas para cada funcionalidade. Isso tornará seu código mais organizado e fácil de entender.
- **Use Estruturas de Dados Apropriadas**: Uma lista pode ser usada para armazenar as tarefas, enquanto uma pilha (ou lista) pode ser útil para gerenciar as tarefas desfeitas e refeitas.
- **Tratamento de Erros**: Certifique-se de implementar tratamento de erros para entradas inválidas, como quando o usuário tenta desfazer uma tarefa quando não há nenhuma tarefa disponível.
- **Persistência de Dados**: Utilize a biblioteca `json` para salvar suas tarefas em um arquivo, facilitando a leitura e a gravação das listas de tarefas.
- **Limpeza da Tela**: Para limpar a tela do console, você pode usar comandos específicos do sistema operacional (`os.system('cls')` no Windows ou `os.system('clear')` no Linux/Mac).
- **Teste Suas Funcionalidades**: À medida que implementa cada função, teste-a individualmente para garantir que esteja funcionando conforme o esperado antes de integrá-la com o resto do programa.
- **Exemplo de Execução**: Teste seu programa com diferentes cenários, como adicionar várias tarefas, desfazer e refazer tarefas, e garantir que a lista seja salva e recarregada corretamente.

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/gerenciador-de-tarefas) ⬅️ 


## Jogo de Adivinhação da Palavra Secreta

### Descrição

Neste exercício, você irá criar um jogo interativo onde o usuário tenta adivinhar uma palavra secreta. Siga as instruções abaixo para implementar o jogo:

1. **Palavra Secreta**: Defina uma palavra secreta que será a meta do jogo.

2. **Entrada do Usuário**: Permita que o usuário digite apenas uma letra por vez. Você deve armazenar as tentativas do usuário.

3. **Conferência de Letras**:
    - Quando o usuário digitar uma letra, você deverá verificar se a letra está presente na palavra secreta.
        - Se a letra digitada estiver na palavra secreta, exiba a letra na sua posição correta.
        - Se a letra não estiver presente, exiba um asterisco (`*`) em seu lugar.

4. **Contagem de Tentativas**: Mantenha um registro do número total de tentativas feitas pelo usuário e exiba essa informação ao final do jogo.

5. **Objetivo do Jogo**: O jogo deve continuar até que o usuário adivinhe todas as letras da palavra secreta ou até que ele decida parar.

### Exemplo de Funcionamento

Suponha que a palavra secreta seja "python":

- O usuário digita `p` → A palavra exibida: `p****`
- O usuário digita `a` → A palavra exibida: `p****` (nenhuma alteração, pois `a` não está na palavra)
- O usuário digita `y` → A palavra exibida: `py***`
- E assim por diante, até que a palavra completa seja adivinhada ou o usuário decida parar.

### Dicas de Implementação

- Use uma lista para armazenar as letras adivinhadas e compare com a palavra secreta.
- Considere usar um loop para continuar solicitando entradas até que a palavra completa seja adivinhada.
- Lembre-se de tratar entradas inválidas (como mais de uma letra ou caracteres especiais).

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/jogo-adivinhacao/solucao.py) ⬅️ 


# Sistema de Perguntas e Respostas

## Descrição do Exercício

Este projeto consiste na criação de um **sistema de perguntas e respostas** no estilo de um jogo. O objetivo do usuário é responder a uma série de perguntas, onde cada uma delas possui opções de resposta. As respostas corretas são armazenadas em um **gabarito**, e o sistema calcula quantas perguntas o usuário acertou ao final do jogo.

### Funcionalidades Principais:
1. **Armazenamento de Perguntas e Respostas**:
   - O sistema deve armazenar um conjunto de perguntas e suas respectivas opções.
   - As respostas corretas devem ser armazenadas em um gabarito.

2. **Apresentação das Perguntas**:
   - As perguntas são exibidas ao usuário uma por vez.
   - Cada pergunta terá um conjunto de opções de respostas para o usuário escolher.

3. **Verificação das Respostas**:
   - Após o usuário selecionar uma resposta, o sistema verifica se a resposta está correta com base no gabarito.

4. **Contador de Acertos**:
   - O sistema deve manter um contador para registrar o número de respostas corretas do usuário.

5. **Resultado Final**:
   - Ao final do jogo, o sistema exibe o número total de perguntas respondidas corretamente pelo usuário.

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/sistema-perguntas-respotas/solucao.py) ⬅️ 

## Sistema de Gerenciamento de Biblioteca

### Descrição

Você deve criar um sistema simples para gerenciar livros em uma biblioteca. O sistema deve ser capaz de adicionar livros, listar livros disponíveis e manter um contador de quantos livros foram adicionados.

**O sistema deve permitir:**

1. **Adicionar livros à biblioteca com informações como título, autor e disponibilidade para empréstimo.**
2. **Manter um controle da quantidade total de livros que foram adicionados à biblioteca.**
3. **Emprestar e devolver livros, alterando seu status de disponibilidade.**
4. **Exibir a disponibilidade de cada livro com uma mensagem apropriada.**
5. **Armazenar e listar todos os livros disponíveis na biblioteca, junto com suas informações e status de disponibilidade.**
6. **Retornar o total de livros adicionados ao sistema de forma global.**
  
### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/sistema-gerenciador-biblioteca/solucao.py) ⬅️ 


## Verificador de Numero Primo

### Descrição

Escreva uma função em Python chamada is_prime que verifique se um número inteiro positivo é primo. Um número primo é aquele que só pode ser dividido por 1 e por ele mesmo, sendo maior que 1.

Em seguida, crie uma lista contendo números inteiros de 2 a 100. Para cada número da lista, utilize a função para verificar se ele é primo ou não, e imprima uma mensagem indicando o resultado, por exemplo: "7 é primo." ou "10 não é primo."

### Dicas para Solucionar o Exercício

1. **Entendimento do Conceito de Número Primo**:
   - Um número primo é aquele que só pode ser dividido por 1 e por ele mesmo. Exemplos: 2, 3, 5, 7, 11, etc.
   - Números menores ou iguais a 1 não são primos.

2. **Função `is_prime(n)`**:
   - **Caso base**: Verifique se o número é menor ou igual a 1. Números menores ou iguais a 1 não são primos, então a função deve retornar `False`.
   
3. **Laço de Verificação**:
   - Para verificar se um número `n` é primo, você precisa testar se ele é divisível por algum número entre 2 e a raiz quadrada de `n`. Isso ocorre porque, se `n` for divisível por algum número maior que sua raiz quadrada, já teria sido detectado por um divisor menor.
   - Use a função `range(2, int(n**0.5) + 1)` para iterar pelos possíveis divisores.

4. **Condicional de Divisibilidade**:
   - Dentro do laço, use a operação de módulo (`%`) para verificar se `n` é divisível por qualquer número no intervalo definido. Se o módulo for igual a zero, `n` não é primo.

5. **Retorno da Função**:
   - Se o número não for divisível por nenhum valor no intervalo, retorne `True`, indicando que o número é primo.

6. **Testando com Vários Números**:
   - Após escrever a função `is_prime`, crie uma lista de números de 2 a 100. Use um laço `for` para passar cada número da lista para a função `is_prime` e imprimir se ele é primo ou não.

7. **Exemplo**:
   - Para o número 29, a raiz quadrada é aproximadamente 5.39, então você precisa testar se 29 é divisível por 2, 3, 4 e 5. Como não é divisível por nenhum desses, a função deve retornar `True`, indicando que 29 é primo.

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/verificador-numero-primo/solucao.py) ⬅️ 


## Sistema de Gestão de Veículos

### Objetivo

Crie um sistema de gestão de veículos que permita gerenciar diferentes tipos de veículos, como carros e caminhões, em uma loja de veículos. O sistema deve ser implementado utilizando Programação Orientada a Objetos (POO) em Python.

### Requisitos

O sistema deve incluir as seguintes funcionalidades:

1. **Classe Veiculo**: 
   - Representa um veículo genérico com os atributos de marca, modelo, preço e estoque. 
   - Deve incluir métodos para vender veículos, adicionar estoque, obter e definir o preço, exibir informações e criar um veículo promocional com 20% de desconto.

2. **Classe Carro**:
   - Herda da classe `Veiculo` e deve incluir um atributo para o número de portas.
   - O método de exibição de informações deve incluir também a quantidade de portas do carro.

3. **Classe Caminhao**:
   - Herda da classe `Veiculo` e deve incluir um atributo para a carga máxima (em toneladas).
   - O método de exibição de informações deve incluir a carga máxima do caminhão.

4. **Classe LojaDeVeiculos**:
   - Representa uma loja que possui um estoque de veículos.
   - Deve incluir métodos para adicionar veículos ao estoque, vender veículos (removendo-os do estoque quando não houver mais unidades) e listar todos os veículos disponíveis na loja.

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/gerenciador-loja-veiculos/solucao.py) ⬅️ 