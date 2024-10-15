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

# coletando um cpf
coleta_cpf = input('Digite seu CPF: ')

# iterando esse cpf para uma lista para poder utilizar o .remove()
lista_cpf = []
for i in coleta_cpf:
    lista_cpf += [i] # em cada letra em coleta_cpf adciona essa letra na lista
    if i == '.': # se for '.' vamos remover
        lista_cpf.remove('.')
    if i == '-': # se for '-' vamos remover
        lista_cpf.remove('-')

#print(type(lista_cpf[0])) # lista tratada mas são str

# tratando os numeros(str) em numeros reais(int)
lista_cpf_int = []
for letra in lista_cpf:
    letra = int(letra) # transformando numerosstr em numeroint
    lista_cpf_int += [letra]

# print(lista_cpf_int)
# print(type(lista_cpf_int[0])) lista com tipo tratado

# precisamos tirar os dois ultimos digitos
# precisamos multiplicar em contagem regressiva em cada numero
# precisamos somar os resultados de todos os numeros
contador_primeiro_digito = 0
multiplicador_primeiro_digito = 10 # multiplicador que sera descrescido a cada rodada
soma_primeiro_digito = 0
while contador_primeiro_digito != 9: # contando ate o primeiro digito
    soma_primeiro_digito += lista_cpf_int[contador_primeiro_digito] * multiplicador_primeiro_digito # somando a multplicacao do algoritmo
    multiplicador_primeiro_digito -= 1 # decrescendo o multiplicador como pede o algoritmo
    contador_primeiro_digito += 1 

# precisamos multiplicar por 10 esse resultado
numero_multiplicado_1 = soma_primeiro_digito * 10

# precisamos descobrir o resto da divisao desse novo resultado por 11
numero_final_1 = numero_multiplicado_1 % 11

# criando variavel para assumir valor de cpf final
# esta servira de comparaçao para ver se o cpf realmenete existe
cpf_correto = lista_cpf_int

# se for maior que 10 o primeiro digito sera 0
# se for menor que 10 o primeiro digito sera o resultado do resto da divisao
cpf_correto[9] = numero_final_1 if numero_final_1 <= 9 else 0
print(f'O primeiro digito deve ser {cpf_correto[9]}')

# o algoritmo do segundo digito preve a inclusao do primeiro digito nas contas
# entao o multiplicador devera ser acrescentado bem como o contador
contador_segundo_digito = 0
multiplicador_segundo_digito = 11 # multiplicador que sera descrescido a cada rodada
soma_segundo_digito = 0
while contador_segundo_digito != 10: # contando ate o primeiro digito
    soma_segundo_digito += lista_cpf_int[contador_segundo_digito] * multiplicador_segundo_digito # somando a multplicacao do algoritmo
    multiplicador_segundo_digito -= 1 # decrescendo o multiplicador como pede o algoritmo
    contador_segundo_digito += 1 

# multiplicando a soma do segundo numero por 10
numero_multiplicado_2 = soma_segundo_digito * 10

# modulo da multiplicacao do segundo numero
numero_final_2 = numero_multiplicado_2 % 11

cpf_correto[10] = numero_final_2 if numero_final_2 <= 9 else 0
print(f'O primeiro digito deve ser {cpf_correto[10]}')

# verificando se o cpf é valido
if cpf_correto == lista_cpf_int:
    print('O CPF inserido está correto')
else:
    print('CPF invalido')


