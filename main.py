from tkinter import *
import random, json
import tkinter
import api as api

def refresh_project_list(opMenu, project_list):
    opMenu['menu'].delete(0, 'end')
    opMenuValue.set('')
    for project in project_list:
        opMenu['menu'].add_command(label=project, command=tkinter._setit(opMenuValue, project))

def update_projects(projects):
    items = api.getAllItems()
    for val in items:
        if val['project_name'] not in projects:
            projects.append(val['project_name'])
            print('Adding Project ' + val['project_name'])
    return projects

def add_item():
    print('Adding...')
    t = text.get()
    project_name = opMenuValue.get()
    if len(project_name) > 0 and len(t) > 0:
        if project_name == 'New Project +':
            def create_project_pressed(top):
                item = {"content": t, "project_name": topText.get()}
                top.destroy()
                api.postItem(item)
                refresh_project_list(opMenu, update_projects(projects))


            print('Creating new project')
            top = Toplevel(app)
            top.geometry('300x150')

            topText = StringVar()

            topEntry = Entry(top, textvariable=topText, width=25)
            topEntry.grid(row=1, column=1)

            topButton = Button(top, text="Create project", command=lambda:create_project_pressed(top))
            topButton.grid(row=1, column=2)
        else:
            item = {"content": t, "project_name": project_name}
            api.postItem(item)
            print("Text: '{0}' added to the database ".format(t))
            print(api.getAllWithProjectName('Colix'))

# Create window object
items = api.getAllItems()
projects = list()
projects = update_projects(projects)
app = Tk()

# Some text and labels
text = StringVar()
label = Label(app, text='Name', font=('bold', 14), pady=20)
label.grid(row=0, column=0, sticky=W)

# Dropdown menu (test) Start
# Set variabels 
opMenuValue = StringVar(app)
opMenuValue.set('general') # default value
opMenu = OptionMenu(app, opMenuValue, *projects)

opMenu.grid(row=0, column=3, sticky=E)
# Dropdown menu (test) END
# Input
entry = Entry(app, textvariable=text)
entry.grid(row=0, column=1)

# Listbox
list = Listbox(app, height=8, width=50)
list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
items = api.getAllItems()


# Scrollbar
# You can also use scrollbar if your want with Scrollbar(app)
# Set it to the listbox with list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=list.yview)

# Buttons
add_btn = Button(app, text="Add", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

# Title of the program
app.title('Oskars Notes')

# Size of the window
app.geometry('700x350')

# Start program
app.mainloop()
