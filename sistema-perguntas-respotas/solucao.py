
"""
Criar um sistema de perguntas e respostas
"""
# Sistema de Perguntas e Respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '12'],
        'Resposta': '2', # Índice da resposta correta
    },
    {
        'Pergunta': 'Quanto é 4/2?',
        'Opções': ['1', '10', '4', '2'],
        'Resposta': '3', # Índice da resposta correta
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '10', '5', '35'],
        'Resposta': '0', # Índice da resposta correta
    }
]

contador_acertos = 0

# Loop para percorrer cada pergunta
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    # Exibe as opções de resposta
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)

    print()

    # Captura a resposta do usuário
    resposta = input('Escolha uma opção: ')
    print()

    # Verifica se a resposta está correta
    if resposta == pergunta['Resposta']:
        print('Você acertou!')
        contador_acertos += 1
    else:
        print('Você errou.')

    print()

# Resultado final
print(f'Você acertou {contador_acertos} de {len(perguntas)} perguntas.')
