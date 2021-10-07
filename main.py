from tkinter import *
from tkinter import ttk
import random, json
import tkinter
import api as api
MAIN_COLOR = (255, 20, 100)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

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

def show_items(*args):
    print('SHOW')
    list.delete(0, END)
    print(opMenuValue)
    items = api.getAllWithProjectName(opMenuValue.get())
    print(items)
    for i in items:
        list.insert('end', i['content'])
    return


def update_item():
    print(list.curselection())
    if list.curselection() != "":
        api.updateItemByQuery({"content": list.get(list.curselection()), "project_name": opMenuValue.get()}, {"content": text.get()})
        show_items()
    return


def delete_item():
    api.deleteItem(opMenuValue.get(), list.get(list.curselection()))
    show_items()
    return


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
        show_items()
    

# Create window object
items = api.getAllItems()
projects = list()
projects = update_projects(projects)
app = Tk()
s = ttk.Style()
s.configure("TMenubutton", background="red")
# Some text and labels
text = StringVar()


# Dropdown menu (test) Start
# Set variabels 
opMenuValue = StringVar(app)
opMenuValue.set('general') # default value
opMenuValue.trace('w', show_items)
opMenu = OptionMenu(app, opMenuValue, *projects)
opMenu.config(font=('Times', 20), fg="#bc6eb8", width=10)

opMenu.grid(row=2, column=6)
# Dropdown menu (test) END
# Input
entry = Entry(app, textvariable=text, font=('Times', 20))
entry.grid(row=1, column=1, pady=20)

# Listbox
list = Listbox(app, height=10, width=70, font=('Times', 20))
list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)


# Scrollbar
# You can also use scrollbar if your want with Scrollbar(app)
# Set it to the listbox with list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=list.yview)

# Buttons
add_btn = Button(app, text="Add", width=8, command=add_item, font=('Times', 20), fg="#6ebc96", bg="#cccccc")
add_btn.grid(row=2, column=0)

# show_btn = Button(app, text="Show", width=8, command=show_items)239 249 235
# show_btn.grid(row=2, column=1, padx=5)

update_btn = Button(app, text="Update", width=8, command=update_item, font=('Times', 20), fg='#6e76bc')
update_btn.grid(row=2, column=1)

delete_btn = Button(app, text="Delete", width=8, command=delete_item, font=('Times', 20), fg="#bc6e72", bg="#cccccc")
delete_btn.grid(row=2, column=2)



# Title of the program
app.title('PyNotes')
icon = PhotoImage(file='icon.png')
app.tk.call('wm', 'iconphoto', app._w, icon)
# Size of the window
app.geometry('1000x450')
show_items()
# Sets the background color
app.config(bg=rgb_hack((204, 204, 204)))
# Start program
app.mainloop()
