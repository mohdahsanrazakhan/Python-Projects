from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.title("To-Do List")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)  # insert at the END
        entry_task.delete(0, END)
    else:
        messagebox.showwarning(
            title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning(
            title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("D:\\Project\\To Do List\\tasks.dat", "rb"))
        listbox_tasks.delete(0, END)
        for task in tasks:
            listbox_tasks.insert(END, task)
    except:
        messagebox.showwarning(
            title="Warning!", message="Cannot find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("D:\\Project\\To Do List\\tasks.dat", "wb"))

# Crate GUI:-


# Frame to hold the widget
frame_tasks = Frame(root)
frame_tasks.pack()

# Listbox section
listbox_tasks = Listbox(frame_tasks, height=10, width=51)
listbox_tasks.pack(side=LEFT)

# Scroll-bar section
scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry section
entry_task = Entry(root, width=53)
entry_task.pack()

# Button section
button_add_task = Button(root, text="Add task", width=45, command=add_task)
button_add_task.pack()

button_delete_task = Button(
    root, text="Delete task", width=45, command=delete_task)
button_delete_task.pack()

button_load_tasks = Button(root, text="Load tasks",
                           width=45, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = Button(root, text="Save tasks",
                           width=45, command=save_tasks)
button_save_tasks.pack()

root.mainloop()

# This project is created by using: tkinter module, Listbox Widget, 
# Scrollbar widget, tkinter.messagebox, Try/Exept Block, pickle
