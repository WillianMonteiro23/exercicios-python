import json

def list_name():
    """Função que lista graficamente o nome da lista"""
    print()
    print('TASK LIST:')
    print()


def list_function(task_list):
    """Função que lista item a item prensete dentro da lista de tarefas"""
    list_name()
    if task_list:
        for item in task_list:
            print(item)   
    else:
        print('THE LIST IS EMPTY') # caso a lista não contenha valores
    print()


def undo_function(task_list):
    """Funcao para desfazer uma tarefa adicionada"""
    list_name()
    try:
        pop_item = task_list.pop(-1) # remove a utlima tarefa adicionada na lista de tarefas
        list_function(task_list)
        return pop_item
    except IndexError: # caso a lista de tarefas estiver vazia trataos o erro, sem quebrar o programa
        print('ERROR : pop from empty list')
    print()


def redo_function(task_list, task_list_pop):
    """Funcao para refazer acao desfeita"""
    list_name()
    if task_list_pop and task_list: # Verifica se task_list_pop é uma lista não vazia
        try:
            list_name()  # Deve ser definida em outro lugar
            task_list.append(task_list_pop.pop())  # Remove e adiciona a última tarefa
            list_function(task_list)  # Deve ser definida em outro lugar
            return task_list
        except Exception as e:  # Captura qualquer erro
            print(f"ERROR: {e} - you don't have command to redo") # retorna o erro cometido
    else:
        print('ERROR: task_list_pop is None or empty.') # caso nao haja elementos na lista de removidos, devolve erro sem quebrar o programa
    print()


def save_function(task_list, file_path):
    """Função que salva a lista na condicao final em um arquivo json"""
    list_name()
    data = task_list
    with open(file_path, 'w', encoding='utf8') as arquivo:
        data = json.dump(task_list, arquivo, indent=2, ensure_ascii=False)
    print('Saved task list.')
    print()
    return data


def read_function(task_list, file_path):
    """Funçao para ler o arquivo json que contenha a lista"""
    data = []
    try:
        with open(file_path, 'r', encoding='utf8') as arquivo:
            data = json.load(arquivo)
    except FileNotFoundError:
        print()
        print('No list saved, creating new list...')
        save_function(task_list,file_path) # caso o arquivo nao exista, criamos o arquivo que receberá a lista de tarefas
    return data

