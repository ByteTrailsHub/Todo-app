while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ").capitalize() + "\n"

            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todo.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todo = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1}. {item}"
                print(row)
        case "edit":
            number = int(input("Enter number of todo: "))
            number = number-1
            new_todo = input("Enter new todo: ").capitalize()
            todos[number] = new_todo
        case "complete":
            number = int(input("Which todo do you want to complete? "))
            todos.pop (number - 1)
        case "exit":
            print("Done, good luck!!!")
            break
