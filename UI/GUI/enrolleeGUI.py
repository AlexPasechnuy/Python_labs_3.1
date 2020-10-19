from tkinter import *

from tkcalendar import Calendar, DateEntry

from UI.GUI.page import Page
from Model.enrollee import Enrollee
from functools import partial

class EnrolleePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        all = Frame(self)
        all.pack(side=LEFT, fill=Y)
        Label(all, text="All enrollees").pack()
        scrollbar = Scrollbar(all)
        scrollbar.pack(side=RIGHT, fill=Y)
        all_listbox = Listbox(all, yscrollcommand=scrollbar.set, width=100)
        all = Enrollee.all()
        for person in all:
            all_listbox.insert(END, person.to_string())
        all_listbox.pack(side="top", fill="both", expand=True)
        scrollbar.config(command=all_listbox.yview)

        #################################################################################################

        find = Frame(self)
        find.pack(side=LEFT, fill=Y)
        Label(find, text="Find enrollee").pack()
        find_entry = Entry(find)
        find_entry.pack()
        find_listbox = Listbox(find, yscrollcommand=scrollbar.set, width=100)
        find_enr = partial(self.find_enr, find_listbox, find_entry)
        find_btn = Button(find, text="Find", command = find_enr).pack()
        scrollbar = Scrollbar(find)
        scrollbar.pack(side=RIGHT, fill=Y)
        find_listbox.pack(side="top", fill="both", expand=True)
        scrollbar.config(command=find_listbox.yview)

        ########################################################################################################

        add = Frame(self)
        add.pack()

        Label(add, text="Add enrollee", font="Helvetica -14 bold").grid(columnspan=2)

        Label(add, text="Surname: ").grid(row=1, column=0)
        surn = Entry(add, width=50)
        surn.grid(row=1, column=1)

        Label(add, text="Name: ").grid(row=2, column=0)
        name = Entry(add, width=50)
        name.grid(row=2, column=1)

        Label(add, text="Patronymic: ").grid(row=3, column=0)
        patr = Entry(add, width=50)
        patr.grid(row=3, column=1)

        Label(add, text="Address: ").grid(row=4, column=0)
        addr = Entry(add, width=50)
        addr.grid(row=4, column=1)

        Label(add, text="Date of birthday: ").grid(row=5, column=0)
        birth = DateEntry(add, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='mm.dd.y')
        birth.grid(row=5, column=1)

        Label(add, text="Number of passport: ").grid(row=6, column=0)
        passp = Entry(add, width=50)
        passp.grid(row=6, column=1)

        add_enr = partial(self.add_enr, surn, name, patr, addr, birth, passp, all_listbox)

        add_btn = Button(add, text="Add enrollee", command =add_enr)
        add_btn.grid(columnspan=2)

    def update_all(self, listbox):
        listbox.delete(0, END)
        for elem in Enrollee.all():
            listbox.insert(END, elem.to_string())
        return

    def find_enr(self, listbox, find_label):
        listbox.delete(0, END)
        for elem in Enrollee.findBySurname(find_label.get()):
            listbox.insert(END, elem.to_string())
        return

    def add_enr(self,surn, name, patr, addr, birth, passp, listbox):
        Enrollee.create(surn.get(), name.get(), patr.get(), addr.get(), birth.get(), passp.get())
        surn.delete(0,END)
        name.delete(0, END)
        patr.delete(0, END)
        addr.delete(0, END)
        birth.delete(0, END)
        passp.delete(0, END)
        self.update_all(listbox)
