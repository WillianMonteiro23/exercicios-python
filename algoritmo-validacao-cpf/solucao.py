"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Coleta o CPF sem pontos e traços e transforma os dígitos em uma lista de inteiros
cpf_input = input('Digite seu CPF (apenas números): ')

# Remove caracteres não numéricos e converte em lista de inteiros
cpf_digits = [int(digit) for digit in cpf_input if digit.isdigit()]

# Verifica se o CPF tem 11 dígitos
if len(cpf_digits) != 11:
    print('CPF inválido! Deve conter 11 dígitos.')
    exit()

# Verifica se o CPF é composto por números repetidos, que são inválidos
if cpf_digits == cpf_digits[::-1] * len(set(cpf_digits)):
    print('CPF inválido! Não pode ser composto por números repetidos.')
    exit()

# Cálculo do primeiro dígito verificador
first_multiplier = 10
first_digit_sum = 0
for i in range(9):  # Multiplica os primeiros 9 dígitos
    first_digit_sum += cpf_digits[i] * first_multiplier
    first_multiplier -= 1

# Multiplica por 10 e tira o módulo por 11
multiplied_number_1 = first_digit_sum * 10
final_number_1 = multiplied_number_1 % 11
first_check_digit = final_number_1 if final_number_1 < 10 else 0

# Cálculo do segundo dígito verificador
# Para calcular o segundo número, o primeiro dígito entra na conta
second_multiplier = 11
second_digit_sum = 0
for i in range(10):  # Multiplica os 9 primeiros dígitos + o primeiro dígito verificador
    second_digit_sum += cpf_digits[i] * second_multiplier
    second_multiplier -= 1

# Multiplica por 10 e tira o módulo por 11
multiplied_number_2 = second_digit_sum * 10
final_number_2 = multiplied_number_2 % 11
second_check_digit = final_number_2 if final_number_2 < 10 else 0

# Verifica se os dígitos verificadores calculados coincidem com os fornecidos
if first_check_digit == cpf_digits[9] and second_check_digit == cpf_digits[10]:
    print('O CPF inserido está correto')
else:
    print('CPF inválido')



















