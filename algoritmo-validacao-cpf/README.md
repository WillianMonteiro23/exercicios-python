# Validador CPF

O Cadastro de Pessoas Físicas (CPF) é um documento utilizado no Brasil para identificar cidadãos. O CPF é composto por 11 dígitos, sendo os 9 primeiros a parte base e os 2 últimos conhecidos como **dígitos verificadores**. O algoritmo de validação do CPF é uma série de cálculos que assegura a integridade do número, evitando fraudes e garantindo que o CPF informado é válido.

## Lógica do Algoritmo

A lógica do algoritmo é baseada em um método de verificação que utiliza os 9 primeiros dígitos do CPF para calcular os dois dígitos verificadores. A ideia é que a sequência de operações matemáticas aplicadas aos dígitos de um CPF válido produza resultados que sempre respeitarão um padrão específico. Esses cálculos não são aleatórios, mas seguem uma regra lógica que permite validar o CPF.

## Cálculo dos Dígitos Verificadores

### Passo 1: Cálculo do Primeiro Dígito Verificador

1. **Multiplicação dos Dígitos**: Os 9 primeiros dígitos do CPF são multiplicados por uma sequência de pesos que começa em 10 e diminui até 2. Por exemplo, se o CPF for `746.824.890`, a multiplicação será:


2. **Soma dos Resultados**: Os produtos são somados para obter um total.

3. **Cálculo do Resto**: O total obtido é multiplicado por 10 e o resto da divisão por 11 é calculado. Este resultado determina o primeiro dígito verificador:
- Se o resultado for menor que 10, esse é o primeiro dígito.
- Se o resultado for 10 ou mais, o primeiro dígito será 0.

### Passo 2: Cálculo do Segundo Dígito Verificador

1. **Inclusão do Primeiro Dígito**: Agora, os 9 primeiros dígitos são somados ao primeiro dígito verificador calculado. A multiplicação segue uma sequência de pesos que começa em 11 e diminui até 2.


2. **Cálculo do Resto**: Assim como no primeiro dígito, o total é multiplicado por 10 e o resto da divisão por 11 é calculado. Este resultado determina o segundo dígito verificador:
- Se o resultado for menor que 10, esse é o segundo dígito.
- Se o resultado for 10 ou mais, o segundo dígito será 0.

## Validação do CPF

Após calcular os dois dígitos verificadores, eles são comparados com os dígitos fornecidos no CPF. Se ambos coincidirem, o CPF é considerado válido; caso contrário, é inválido.