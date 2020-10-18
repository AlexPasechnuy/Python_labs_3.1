from tkinter import *
from tkinter.ttk import Notebook

from UI.GUI.page import Page

class Examiner(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       all = Frame(self)
       all.pack(side=LEFT, fill=Y)
       Label(all, text="All examiners").pack()
       scrollbar = Scrollbar(all)
       scrollbar.pack(side=RIGHT, fill=Y)
       languages_listbox = Listbox(all, yscrollcommand=scrollbar.set, width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           languages_listbox.insert(END, language)
       languages_listbox.pack(side="top", fill="both", expand=True)
       scrollbar.config(command=languages_listbox.yview)

       #################################################################################################

       find = Frame(self)
       find.pack(side=LEFT, fill=Y)
       Label(find, text="Find examiner").pack()
       find_entry = Entry(find).pack()
       scrollbar = Scrollbar(find)
       scrollbar.pack(side=RIGHT, fill=Y)
       languages_listbox = Listbox(find, yscrollcommand=scrollbar.set, width=100)
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

       Label(add, text="Add examiner", font="Helvetica -14 bold").grid(columnspan = 2)

       Label(add, text="Surname: ").grid(row=1, column=0)
       surn = Entry(add, width=50).grid(row=1, column=1)

       Label(add, text="Name: ").grid(row=2, column=0)
       name = Entry(add, width=50).grid(row=2, column=1)

       Label(add, text="Patronymic: ").grid(row=3, column=0)
       patr = Entry(add, width=50).grid(row=3, column=1)

       Label(add, text="Salary: ").grid(row=4, column=0)
       sal = Entry(add, width=50).grid(row=4, column=1)

       add_btn = Button(add, text="Add examiner").grid(columnspan = 2)