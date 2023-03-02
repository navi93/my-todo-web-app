def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as new_file:
        todos_local = new_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


