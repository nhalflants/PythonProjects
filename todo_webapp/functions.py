FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of items. """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def save_todos(todos_args, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_args)
