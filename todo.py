class todo:
    def __init__(self):
        self.todos = []

    def add_task(self):
        task = input("Titulo da tarefa: ")
        self.todos.append(task)

    def remove_task(self):
        print(self.todos)
        task = int((input("Qual id da task que quer excluir: ")))
        self.todos.pop(task)

    def show_tasks(self):
        print(self.todos)


    def clear_tasks(self):
       self.todos.clear()
           
def main():
    todo_list = todo()
    user_input = 0
    while user_input != 5:
        user_input = int(input("""
    Escolha uma opção
                                
                                1- adicionar uma tarefa
                                2- remover uma tarefa
                                3- mostrar tarefas
                                4- limpar todas as tarefas
                                5- fechar
    """))
        if user_input == 1:
            todo_list.add_task()
        elif user_input == 2:
            todo_list.remove_task()
        elif user_input == 3:
            todo_list.show_tasks()
        elif user_input == 4:
            todo_list.clear_tasks()
        elif user_input > 4 or user_input < 0:
            break
main()


