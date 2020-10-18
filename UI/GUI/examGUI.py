from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from UI.GUI.page import Page

class Exam(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       all = Frame(self)
       all.pack(side=LEFT, fill=Y)
       Label(all, text="All exams").pack()
       scrollbar = Scrollbar(all)
       scrollbar.pack(side=RIGHT, fill=Y)
       all_listbox = Listbox(all, yscrollcommand=scrollbar.set, width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           all_listbox.insert(END, language)
       all_listbox.pack(side="top", fill="both", expand=True)
       scrollbar.config(command=all_listbox.yview)

#################################################################################################

       find = Frame(self)
       find.pack(side=LEFT, fill=Y)
       Label(find, text="Find exam").pack()
       scrollbar = Scrollbar(find)
       scrollbar.pack(side=RIGHT, fill=Y)
       find_listbox = Listbox(find, yscrollcommand=scrollbar.set, width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           find_listbox.insert(END, language)
       find_listbox.pack(side="top", fill="both", expand=True)
       scrollbar.config(command=find_listbox.yview)

       ########################################################################################################

       add = Frame(self)
       add.pack()

       Label(add, text="Add exam", font="Helvetica -14 bold").grid(columnspan = 3)

       Label(add, text="Time of pass(DD.MM.YYYY HH:MM): ").grid(row=1, column=0)
       time = Entry(add, width=50).grid(row=1, column=1, columnspan = 2)

       Label(add, text="Name of exam: ").grid(row=2, column=0)
       name = Entry(add, width=50).grid(row=2, column=1, columnspan = 2)

       Label(add, text="Score: ").grid(row=3, column=0)
       score = Entry(add, width=50).grid(row=3, column=1, columnspan = 2)

       Label(add, text="Enrollee: ").grid(row=4, column=0)
       enr = Entry(add, width=50).grid(row=4, column=1)
       find_enr_btn = Button(add, text = "Find").grid(row = 4, column = 2)
       scrollbar = Scrollbar(add)
       scrollbar.grid()
       enrolee_listbox = Listbox(add, yscrollcommand=scrollbar.set, width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           enrolee_listbox.insert(END, language)
       enrolee_listbox.grid(row = 5, column = 0, columnspan = 3)
       scrollbar.config(command=enrolee_listbox.yview)

       Label(add, text="Examiner: ").grid(row=6, column=0)
       examiner = Entry(add, width=50).grid(row=6, column=1)
       find_examiner_btn = Button(add, text = "Find").grid(row = 6, column = 2)
       scrollbar = Scrollbar(add)
       scrollbar.grid()
       examiner_listbox = Listbox(add, yscrollcommand=scrollbar.set, width=100)
       languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
                    "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
                    "T-SQL", "PL-SQL", "Typescript"]
       for language in languages:
           examiner_listbox.insert(END, language)
       examiner_listbox.grid(row = 7, column = 0, columnspan = 3)
       scrollbar.config(command=examiner_listbox.yview)
       add_btn = Button(add, text="Add exam").grid(columnspan = 3)