import functions
import time
import PySimpleGUI as Sg

# Window elements definition
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter a todo", key="todo")
add_button = Sg.Button("Add")

# Window definition
window = Sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button]],
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
        case Sg.WIN_CLOSED:
            break

window.close()
