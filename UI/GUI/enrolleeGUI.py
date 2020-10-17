from tkinter import *
from tkinter.ttk import Notebook

from UI.GUI.page import Page

class Enrollee(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       all = Frame(self)
       all.pack(side = LEFT, fill = Y)
       all_title = Label(all, text = "All enrollees")
       all_title.pack()
       scrollbar = Scrollbar(all)
       scrollbar.pack(side=RIGHT, fill=Y)
       languages_listbox = Listbox(all, yscrollcommand=scrollbar.set,  width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           languages_listbox.insert(END, language)
       languages_listbox.pack(side="top", fill="both", expand=True)
       scrollbar.config(command=languages_listbox.yview)

#################################################################################################

       find = Frame(self)
       find.pack(side = LEFT, fill = Y)
       find_title = Label(find, text = "Find enrollee")
       find_title.pack()
       scrollbar = Scrollbar(find)
       scrollbar.pack(side=RIGHT, fill=Y)
       languages_listbox = Listbox(find, yscrollcommand=scrollbar.set,  width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           languages_listbox.insert(END, language)
       languages_listbox.pack(side="top", fill="both", expand=True)
       scrollbar.config(command=languages_listbox.yview)

########################################################################################################

       add = Frame(self)
       add.pack()

       add_title = Label(add, text = "Add enrollee", font = "Helvetica -14 bold")
       add_title.grid()

       surn_title = Label(add, text = "Surname: ")
       surn_title.grid(row = 1, column = 0)
       surn = Entry(add, width = 50)
       surn.grid(row = 1, column = 1)

       name_title = Label(add, text = "Name: ")
       name_title.grid(row = 2, column = 0)
       name = Entry(add, width = 50)
       name.grid(row = 2, column = 1)

       patr_title = Label(add, text = "Patronymic: ")
       patr_title.grid(row = 3, column = 0)
       patr = Entry(add, width = 50)
       patr.grid(row = 3, column = 1)

       addr_title = Label(add, text = "Address: ")
       addr_title.grid(row = 4, column = 0)
       addr = Entry(add, width = 50)
       addr.grid(row = 4, column = 1)

       birth_title = Label(add, text = "Date of birthday: ")
       birth_title.grid(row = 5, column = 0)
       birth = Entry(add, width = 50)
       birth.grid(row = 5, column = 1)

       passp_title = Label(add, text = "Number of passport: ")
       passp_title.grid(row = 6, column = 0)
       passp = Entry(add, width = 50)
       passp.grid(row = 6, column = 1)

       add_btn = Button(add, text = "Add enrollee")
       add_btn.grid()