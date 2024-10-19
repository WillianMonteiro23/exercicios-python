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

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/algoritmo-validacao-cpf/validador_cpf.py) ⬅️ 


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

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/jogo_adivinhacao.py) ⬅️ 

