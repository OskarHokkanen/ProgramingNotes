from tkinter import *
import random, json
import api as api


def add_item():
    print('Adding...')
    t = text.get()
    project_name = opMenuValue.get()
    if len(project_name) > 0:
        item = {"content": t, "project_name": project_name}
        api.postItem(item)
        print("Text: '{0}' added to the database ".format(t))
        print(api.getAllWithProjectName('Colix'))

# Create window object
items = api.getAllItems()
projects = list()
for val in items:
    if val['project_name'] not in projects:
        projects.append(val['project_name'])
        print('Adding Project ' + val['project_name'])

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
