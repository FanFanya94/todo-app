import functions
import time
import PySimpleGUI as Sg

# Window elements definition
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter a todo", key="todo")
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")
list_box = Sg.Listbox(values=functions.get_list_from_textfile(), key="list",
                      enable_events=True, size=(45, 10))

# Window definition
window = Sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button],
                           [list_box, edit_button]],
                   font=("Helvetica", 20))

# Window run
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_list_from_textfile()
            new_todo = values["todo"]
            todos.append(new_todo)
            functions.save_list_to_file(todos)
            window["list"].update(values=todos)
        case "Edit":
            todo_to_edit = values["list"][0]
            new_todo_instead = values["todo"]

            todos = functions.get_list_from_textfile()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo_instead
            functions.save_list_to_file(todos)
            window["list"].update(values=todos)
        case "list":
            window["todo"].update(value=values["list"][0])
        case Sg.WIN_CLOSED:
            break

window.close()
