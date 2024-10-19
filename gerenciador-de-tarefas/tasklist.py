# Gerenciador de Tarefas

#Importações do módulo functions_tasklist e os para usar funçoes criadas e clear(cls)
from tasklist_functions import list_name , list_function, undo_function, redo_function, save_function, read_function
import os

# Inicializa a variável option como uma string vazia
option = ''  

# Lista de comandos disponíveis no gerenciador de tarefas
commands = ["list", "undo", "redo", "clear", "save", "stop"]

# Caminho do arquivo onde a lista de tarefas será salva
FILE_PATH = 'task_list.json'

# Inicializa a variável task_list chamando a função read_function,
# que lê as tarefas do arquivo FILE_PATH ou retorna uma lista vazia se o arquivo estiver vazio
task_list = read_function([], FILE_PATH)

# Inicializa uma lista vazia para armazenar tarefas que foram desfeitas
task_list_pop = []  

# loop até que o usuário deseja encerrar o gerenciador
while option != 'stop':


    print(f'Commands: {commands[0]}, {commands[1]}, {commands[2]}, {commands[3]}, {commands[4]} or {commands[5]}')
    option = input('Enter a task or command:  ')

    # caso a opção do usuario nao seja nenhum comando, o texto digitado sera adcionado na lista de tarefas
    if option not in commands:
        task_list.append(option)
        list_name()
        for item in task_list:
            print(item)
        print()

    # caso a opçao seja list entao a funcao list_function é chamada
    elif option == 'list':
        list_function(task_list)

    # caso a opcao seja undo entao undo_function é chamada
    elif option == 'undo':
        task_list_pop.append(undo_function(task_list))
    
    # caso a opcao seja redo entao redo_function é chamada
    elif option == 'redo':
        redo_function(task_list, task_list_pop)

    # caso a opcao seja clear entao utilizamos a funcao da biblioteca os, cls(ou clear) que limpa o prompt
    elif option == 'clear':
        os.system('cls')

    # caso a opcao seja save entao save_function é chamada, salvando toda a lista em um arquivo json no caminho indicado
    elif option == 'save':
        save_function(task_list, FILE_PATH)



