import functions
import time

current_date_and_time = time.strftime("%B %d, %Y %H:%M:%S")
print("It's", current_date_and_time)

todos = functions.get_list_from_textfile()

while True:
    user_action = input('Type "add", "show", "edit", "complete", "save", "clear" or "exit": ')
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[3:].strip()
        if len(todo) > 0:
            todos.append(todo)

    elif user_action.startswith("show"):
        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[8:].strip()) - 1
            if number < len(todos):
                del todos[number]
            else:
                print("There is no item with that number")
                continue

        except ValueError:
            print("To complete an item please enter the keyword 'complete' "
                  "and then the number of item you want complete")
            continue

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:].strip()) - 1
            if number < len(todos):
                todos[number] = input("Enter new todo: ")
            else:
                print("There is no item with that number")
                continue

        except TypeError:
            print("To edit an item please enter the keyword 'edit' "
                  "and then the number of item you want edit")
            continue

        except ValueError:
            print("To edit an item please enter the keyword 'edit' "
                  "and then the number of item you want edit")
            continue

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("save"):
        functions.save_list_to_file(todos)
        print("File was saved.")

    elif user_action.startswith("exit"):
        functions.save_list_to_file(todos)
        break

    elif user_action.startswith("clear"):
        todos.clear()
        print("The list was cleaned.")

    else:
        print("Invalid command.")

print("Buy!")
