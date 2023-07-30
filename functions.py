# Making 2 functions for the to-do CLI and GUI.

def get_todos(file_path="todos.txt"):
    """
    Makes the "todos.txt" as a list
    Returns a list of todos
    """

    with open(file_path) as file_local:
        todos_local = file_local.readlines()
        new_todos = []
        for todo in todos_local:
            new_todos.append(todo.title())
        return new_todos


def write_todos(todos_arg, file_path="todos.txt"):
    """
    Overwriting the "todos.txt" with the updated list.
    """
    new_todo = []
    for todo in todos_arg:
        new_todo.append(todo.title())
    with open(file_path, "w") as file:
        file.writelines(todos_arg)


def show_todos():
    """
    Showing the list with the lines numbered.
    """

    todos = get_todos()
    for line, todo in enumerate(todos, 1):
        todo = todo.strip("\n")
        todo = todo.capitalize()
        print(f"{line}. {todo}")