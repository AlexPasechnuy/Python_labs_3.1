from tkinter import *
from tkinter import messagebox

from tkcalendar import Calendar, DateEntry

from UI.GUI.page import Page
from Model.examiner import Examiner
from functools import partial

class ExaminerPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        all = Frame(self)
        all.pack(side=LEFT, fill=Y)
        Label(all, text="All examiners").pack()
        self.all_listbox = Listbox(all, width=100)
        self.all_listbox.bind('<Double-1>', self.all_list_on_click)
        self.all_list = Examiner.all()
        for person in self.all_list:
            self.all_listbox.insert(END, person.to_string())
        self.all_listbox.pack(side="top", fill="both", expand=True)
        all_report = Button(all, text = "Export info about all examiners in Excel")
        all_report.pack(side="top")

        #################################################################################################

        find = Frame(self)
        find.pack(side=LEFT, fill=Y)
        Label(find, text="Find examiner").pack()
        find_entry = Entry(find)
        find_entry.pack()
        self.find_listbox = Listbox(find, width=100)
        self.find_listbox.bind('<Double-1>', self.find_list_on_click)
        find_examiner = partial(self.find_examiner, self.find_listbox, find_entry)
        find_btn = Button(find, text="Find", command = find_examiner).pack()
        self.find_listbox.pack(side="top", fill="both", expand=True)

        ########################################################################################################

        add = Frame(self)
        add.pack()

        Label(add, text="Add examiner", font="Helvetica -14 bold").grid(columnspan=2)

        Label(add, text="Surname: ").grid(row=1, column=0)
        surn = Entry(add, width=50)
        surn.grid(row=1, column=1)

        Label(add, text="Name: ").grid(row=2, column=0)
        name = Entry(add, width=50)
        name.grid(row=2, column=1)

        Label(add, text="Patronymic: ").grid(row=3, column=0)
        patr = Entry(add, width=50)
        patr.grid(row=3, column=1)

        Label(add, text="Salary: ").grid(row=4, column=0)
        salary = Entry(add, width=50)
        salary.grid(row=4, column=1)

        add_examiner = partial(self.add_examiner, surn, name, patr, salary, self.all_listbox)

        add_btn = Button(add, text="Add examiner", command =add_examiner)
        add_btn.grid(columnspan=2)

    def update_all(self, listbox):
        listbox.delete(0, END)
        self.all_list = Examiner.all()
        for elem in self.all_list:
            listbox.insert(END, elem.to_string())
        return

    def find_examiner(self, listbox, find_label):
        listbox.delete(0, END)
        self.find_list = Examiner.findBySurname(find_label.get())
        for elem in self.find_list:
            listbox.insert(END, elem.to_string())
        return

    def add_examiner(self, surn, name, patr, salary, listbox):
        Examiner.create(surn.get(), name.get(), patr.get(), int(salary.get()))
        surn.delete(0,END)
        name.delete(0, END)
        patr.delete(0, END)
        salary.delete(0, END)
        self.update_all(listbox)

    def all_list_on_click(self, event):
        cs = self.all_listbox.curselection()
        self.manipulateExaminer(self.all_list[cs[0]])

    def find_list_on_click(self, event):
        cs = self.find_listbox.curselection()
        self.manipulateExaminer(self.find_list[cs[0]])

    def manipulateExaminer(self, chosenExaminer):
        newWindow = Toplevel(self)
        newWindow.title("New Window")
        newWindow.geometry("1000x500")
        exams = Frame(newWindow)
        exams.pack(side=LEFT, fill=Y)
        Label(exams, text="Exams of examiner:").pack()
        exams_listbox = Listbox(exams, width=106)
        for person in chosenExaminer.get_exams():
            exams_listbox.insert(END, person.to_string())
        exams_listbox.pack(side=LEFT, fill="both", expand=True)
        change = Frame(newWindow)
        change.pack(side=RIGHT, fill="both")
        Label(change, text = "Change address").grid(row = 0, columnspan = 2)
        Label(change, text="Enter new address: ").grid(row = 1, column = 0)
        new_sal = Entry(change, width = "39")
        new_sal.delete(0, END)
        new_sal.insert(0, chosenExaminer.payment)
        new_sal.grid(row = 1, column = 1)
        change_sal = partial(self.change_salary, new_sal, chosenExaminer)
        change_sal_btn = Button(change, text = "Change salary", command=change_sal)
        change_sal_btn.grid(columnspan = 2)
        Label(change, text="------------------------------------------------------------").grid(columnspan = 2)
        delete = partial(self.delete_examiner, chosenExaminer)
        del_btn = Button(change, text = "Delete examiner", command=delete)
        del_btn.grid(columnspan = 2)
        Label(change, text="------------------------------------------------------------").grid(columnspan=2)
        enr_report = Button(change, text = "Export info about this examiner in Word")
        enr_report.grid(columnspan = 2)

    def change_salary(self, sal_entry, chosenEnrollee):
        chosenEnrollee.change_payment(int(sal_entry.get()))
        self.update_all(self.all_listbox)

    def delete_examiner(self, chosenExaminer):
        result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if result == 'yes':
            chosenExaminer.delete();
        else:
            return
        self.update_all(self.all_listbox)