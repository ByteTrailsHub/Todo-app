while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + '\n'

            with open('Todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('Todo.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('Todo.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.capitalize()
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)
        case "edit":
            number = int(input("Enter the number of todo to change: "))
            number = number -1

            with open('Todo.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            with open('Todo.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Enter the number of todo to complete: "))

            with open('Todo.txt', 'r') as file:
                todos = file.readlines()
            index = number -1
            todo_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('Todo.txt', 'w') as file:
                file.writelines(todos)
            message = f'Todo {todo_remove} was removed from the list.'
            print(message)
            
        case "exit":
            print("Done, good luck!!!")
            break
