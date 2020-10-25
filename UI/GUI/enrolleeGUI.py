from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

from UI.GUI.page import Page
from Model.enrollee import Enrollee
from functools import partial

import datetime as dt

class EnrolleePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        all = Frame(self)
        all.pack(side=LEFT, fill=Y)
        Label(all, text="All enrollees").pack()
        self.all_listbox = Listbox(all, width=100)
        self.all_listbox.bind('<Double-1>', self.all_list_on_click)
        self.all_list = Enrollee.all()
        for person in self.all_list:
            self.all_listbox.insert(END, person.to_string())
        self.all_listbox.pack(side="top", fill="both", expand=True)

        #################################################################################################

        find = Frame(self)
        find.pack(side=LEFT, fill=Y)
        Label(find, text="Find enrollee").pack()
        find_entry = Entry(find)
        find_entry.pack()
        self.find_listbox = Listbox(find, width=100)
        self.find_listbox.bind('<Double-1>', self.find_list_on_click)
        find_enr = partial(self.find_enr, self.find_listbox, find_entry)
        find_btn = Button(find, text="Find", command = find_enr).pack()
        self.find_listbox.pack(side="top", fill="both", expand=True)

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
        birth = DateEntry(add, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd.mm.y')
        birth.grid(row=5, column=1)

        Label(add, text="Number of passport: ").grid(row=6, column=0)
        passp = Entry(add, width=50)
        passp.grid(row=6, column=1)

        add_enr = partial(self.add_enr, surn, name, patr, addr, birth, passp, self.all_listbox)

        add_btn = Button(add, text="Add enrollee", command =add_enr)
        add_btn.grid(columnspan=2)

    def update_all(self, listbox):
        listbox.delete(0, END)
        self.all_list = Enrollee.all()
        for elem in self.all_list:
            listbox.insert(END, elem.to_string())
        return

    def find_enr(self, listbox, find_label):
        listbox.delete(0, END)
        self.find_list = Enrollee.findBySurname(find_label.get())
        for elem in self.find_list:
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

    def all_list_on_click(self, event):
        cs = self.all_listbox.curselection()
        messagebox.showinfo("Title", self.all_list[cs[0]].to_string())

    def find_list_on_click(self, event):
        cs = self.find_listbox.curselection()
        messagebox.showinfo("Title", self.find_list[cs[0]].to_string())
