from functions import get_todos, save_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now,", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")
        save_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            new_todo = input("Enter new todo: ")

            todos = get_todos()

            todos[number - 1] = new_todo + "\n"

            save_todos(todos)
        except ValueError:
            print("Your command isn't valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todos.pop(number - 1)
            save_todos(todos)
        except IndexError:
            print("There is no item with this number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Unknown command")
