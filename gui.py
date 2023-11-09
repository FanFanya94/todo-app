import functions
import time
import PySimpleGUI as Sg

# Get todos list from file
todos = functions.get_list_from_textfile()

# Window elements definition
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter a todo", key="todo")
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")
save_button = Sg.Button("Save")
list_box = Sg.Listbox(values=functions.indexate_list(todos), key="list",
                      enable_events=True, size=(45, 10))

# Window definition
window = Sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button],
                           [list_box, edit_button],
                           [save_button]],
                   font=("Helvetica", 20))

# Window run
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            new_todo = values["todo"]
            todos.append(new_todo)
            window["list"].update(values=functions.indexate_list(todos))
        case "Edit":
            index_of_todo_to_edit = int(values["list"][0][0].strip('.'))
            new_todo_instead = values["todo"]
            todos[index_of_todo_to_edit - 1] = new_todo_instead
            window["list"].update(values=functions.indexate_list(todos))
        case "list":
            window["todo"].update(value=values["list"][0][1])
        case "Save":
            functions.save_list_to_file(todos)
        case Sg.WIN_CLOSED:
            break

window.close()
