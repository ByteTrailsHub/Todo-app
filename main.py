def get_todos():
    with open('todo.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index +1}. {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop (index)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"You've completed {todo_to_remove} and it was removed from the list!"
            print(message)
        except IndexError:
            print("There's no todo with that number!")
            continue

    elif user_action.startswith('exit'):
        print("Done, good luck!!!")
        break
    else:
        print("This command is not valid!")
