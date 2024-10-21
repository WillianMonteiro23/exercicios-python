"""
Números Primos: Escreva uma função que verifique se um número é primo.
Teste a função com uma lista de números ate 100.
"""
def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 11, 13, 14, 15, 16, 17, 19, 20, 23, 24, 25, 29]

for number in numbers:
    if is_prime(number):
        print(f"{number} é primo.")
    else:
        print(f"{number} não é primo.")
