
## Jogo de Adivinhação da Palavra Secreta

### Descrição

Escreva uma função em Python chamada is_prime que verifique se um número inteiro positivo é primo. Um número primo é aquele que só pode ser dividido por 1 e por ele mesmo, sendo maior que 1.

Em seguida, crie uma lista contendo números inteiros de 2 a 100. Para cada número da lista, utilize a função para verificar se ele é primo ou não, e imprima uma mensagem indicando o resultado, por exemplo: "7 é primo." ou "10 não é primo."

### Dicas para Solucionar o Exercício de Número Primo

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

### ➡️ [Solução](https://github.com/WillianMonteiro23/exercicios-python/blob/main/jogo-adivinhacao/jogo_adivinhacao.py) ⬅️ 