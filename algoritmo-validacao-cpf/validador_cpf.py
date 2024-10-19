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
coleta_cpf = input('Digite seu CPF (apenas números): ')

# Remove caracteres não numéricos e converte em lista de inteiros
cpf_base = [int(digito) for digito in coleta_cpf if digito.isdigit()]

# Verifica se o CPF tem 11 dígitos
if len(cpf_base) != 11:
    print('CPF inválido! Deve conter 11 dígitos.')
    exit()

# Verifica se o CPF é composto por números repetidos, que são inválidos
if cpf_base == cpf_base[::-1] * len(set(cpf_base)):
    print('CPF inválido! Não pode ser composto por números repetidos.')
    exit()

# Cálculo do primeiro dígito verificador
multiplicador_primeiro_digito = 10
soma_primeiro_digito = 0
for i in range(9):  # Multiplica os primeiros 9 dígitos
    soma_primeiro_digito += cpf_base[i] * multiplicador_primeiro_digito
    multiplicador_primeiro_digito -= 1

# Multiplica por 10 e tira o módulo por 11
numero_multiplicado_1 = soma_primeiro_digito * 10
numero_final_1 = numero_multiplicado_1 % 11
primeiro_digito_verificador = numero_final_1 if numero_final_1 < 10 else 0

# Cálculo do segundo dígito verificador
# Para calcular o segundo número, o primeiro dígito entra no a conta
multiplicador_segundo_digito = 11
soma_segundo_digito = 0
for i in range(10):  # Multiplica os 9 primeiros dígitos + o primeiro dígito verificador
    soma_segundo_digito += cpf_base[i] * multiplicador_segundo_digito
    multiplicador_segundo_digito -= 1

# Multiplica por 10 e tira o módulo por 11
numero_multiplicado_2 = soma_segundo_digito * 10
numero_final_2 = numero_multiplicado_2 % 11
segundo_digito_verificador = numero_final_2 if numero_final_2 < 10 else 0

# Verifica se os dígitos verificadores calculados coincidem com os fornecidos
if primeiro_digito_verificador == cpf_base[9] and segundo_digito_verificador == cpf_base[10]:
    print('O CPF inserido está correto')
else:
    print('CPF inválido')


















