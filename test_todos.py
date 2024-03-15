import test_todos
from todo import *
def test_add_task():
    todo_list = todo()
    todo_list.add_task("Tarefa 1")
    assert "Tarefa 1" in todo_list.todos


def test_remove_task():
    todo_list = todo()
    todo_list.add_task("Tarefa 1")
    todo_list.remove_task(0)
    assert len(todo_list.todos) == 0


def test_show_tasks():
    todo_list = todo()
    todo_list.add_task("Tarefa 1")
    todo_list.add_task("Tarefa 2")
    todo_list.show_tasks()


def test_clear_tasks():
    todo_list = todo()
    todo_list.add_task("Tarefa 1")
    todo_list.add_task("Tarefa 2")
    todo_list.clear_tasks()
    assert len(todo_list.todos) == 0


if __name__ == "__main__":
    test_todos.main()
