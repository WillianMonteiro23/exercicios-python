import os  # Importando os para limpar o terminal

def limpar_terminal():
    """Limpa o terminal"""
    os.system('cls')

def solicitar_letra():
    """Solicita ao usuário uma letra e verifica a entrada"""
    while True:
        letra = input('Digite uma letra: ')
        
        # Verifica se a entrada é um número
        if letra.isdigit():
            print('Você digitou um número, digite uma LETRA')
            continue
        
        # Verifica se o usuário digitou apenas uma letra
        if len(letra) != 1:
            print('Digite apenas UMA letra')
            continue
        
        return letra.lower()  # Retorna a letra em minúscula

def atualizar_palavra_formada(palavra_secreta, letras_acertadas):
    """Atualiza a palavra formada com base nas letras acertadas"""
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    return palavra_formada

def jogar():
    """Função principal do jogo"""
    palavra_secreta = 'python'
    letras_acertadas = ''
    contador = 0

    while True:
        letra_digitada = solicitar_letra()  # Solicita uma letra ao usuário
        contador += 1  # Contador de tentativas

        # Adiciona letra digitada se estiver na palavra secreta
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        # Atualiza a palavra formada
        palavra_formada = atualizar_palavra_formada(palavra_secreta, letras_acertadas)

        # Mostra a palavra formada ao usuário
        print('Palavra: ', palavra_formada)

        # Verifica se o usuário acertou a palavra
        if palavra_formada == palavra_secreta:
            limpar_terminal()
            print('PARABÉNS! Você acertou a palavra, era', palavra_secreta)
            print('Total de tentativas:', contador)
            break  # Sai do loop quando a palavra é adivinhada

if __name__ == "__main__":
    jogar()