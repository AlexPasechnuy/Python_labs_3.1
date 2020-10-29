from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from functools import partial
from tkinter import messagebox

from UI.GUI.page import Page
from Model.exam import Exam
from Model.enrollee import Enrollee
from Model.examiner import Examiner

class ExamPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        all = Frame(self)
        all.pack(side=LEFT, fill=Y)
        Label(all, text="All exams").pack()
        self.all_listbox = Listbox(all, width=100)
        self.all_listbox.bind('<Double-1>', self.all_list_on_click)
        self.all_list = Exam.all()
        for person in self.all_list:
            self.all_listbox.insert(END, person.to_string())
        self.all_listbox.pack(side="top", fill="both", expand=True)

        #################################################################################################

        find = Frame(self)
        find.pack(side=LEFT, fill=Y)
        Label(find, text="Find exam").pack()
        find_entry = DateEntry(find, width=12, background='darkblue', foreground='white', borderwidth=2,
                               date_pattern='dd.mm.y')
        find_entry.pack()
        self.find_listbox = Listbox(find, width=100)
        self.find_listbox.bind('<Double-1>', self.find_list_on_click)
        find_enr = partial(self.find_exam, self.find_listbox, find_entry)
        find_btn = Button(find, text="Find", command=find_enr).pack()
        self.find_listbox.pack(side="top", fill="both", expand=True)

        ########################################################################################################

        add = Frame(self)
        add.pack()

        Label(add, text="Add exam", font="Helvetica -14 bold").grid(columnspan=3)

        Label(add, text="Date of pass: ").grid(row=1, column=0)
        date = DateEntry(add, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd.mm.y')
        date.grid(row = 1, column = 1)

        Label(add, text="Time of pass(HH:MM): ").grid(row=2, column=0)
        time = Entry(add, width=50)
        time.grid(row=2, column=1, columnspan=2)

        Label(add, text="Name of exam: ").grid(row=3, column=0)
        name = Entry(add, width=50)
        name.grid(row=3, column=1, columnspan=2)

        Label(add, text="Score: ").grid(row=4, column=0)
        score = Entry(add, width=50)
        score.grid(row=4, column=1, columnspan=2)

        Label(add, text="Enrollee: ").grid(row=5, column=0)
        enrollee_entry = Entry(add, width=50)
        enrollee_entry.grid(row=5, column=1)
        self.enrollee_listbox = Listbox(add, width=100)
        find_enr = partial(self.find_enrollee, self.enrollee_listbox, enrollee_entry)
        find_enr_btn = Button(add, text="Find", command = find_enr).grid(row=5, column=2)
        self.enrollee_listbox.grid(row=6, column=0, columnspan=3)
        self.enrollee_listbox.bind('<Double-1>', self.find_enrollee_on_click)
        self.chosen_enrollee_text = StringVar()
        self.chosen_enrollee_label = Label(add, textvariable = self.chosen_enrollee_text).grid(row = 7)

        Label(add, text="Examiner: ").grid(row=8, column=0)
        examiner_entry = Entry(add, width=50)
        examiner_entry.grid(row=8, column=1)
        self.examiner_listbox = Listbox(add, width=100)
        find_examiner = partial(self.find_examiner, self.examiner_listbox, examiner_entry)
        find_examiner_btn = Button(add, text="Find", command = find_examiner).grid(row=8, column=2)
        self.examiner_listbox.grid(row=9, column=0, columnspan=3)
        self.examiner_listbox.bind('<Double-1>', self.find_examiner_on_click)
        self.chosen_examiner_text = StringVar()
        self.chosen_examiner_label = Label(add, textvariable = self.chosen_examiner_text).grid(row = 10)

        add_exam = partial(self.add_exam, date, time, name, score, enrollee_entry, examiner_entry, self.all_listbox)
        add_btn = Button(add, text="Add exam", command = add_exam).grid(columnspan=3)

    def find_exam(self, listbox, find_label):
        listbox.delete(0, END)
        self.find_list = Exam.find_by_date(find_label.get())
        for elem in self.find_list:
            listbox.insert(END, elem.to_string())
        return

    def find_enrollee(self, listbox, find_label):
        listbox.delete(0, END)
        self.find_enrollee_list = Enrollee.findBySurname(find_label.get())
        for elem in self.find_enrollee_list:
            listbox.insert(END, elem.to_string())
        return

    def find_examiner(self, listbox, find_label):
        listbox.delete(0, END)
        self.find_examiner_list = Examiner.findBySurname(find_label.get())
        for elem in self.find_examiner_list:
            listbox.insert(END, elem.to_string())
        return

    def update_all(self, listbox):
        listbox.delete(0, END)
        self.all_list = Exam.all()
        for elem in self.all_list:
            listbox.insert(END, elem.to_string())
        return

    def add_exam(self, date, time, name, score_label, enrollee_find, examiner_find, listbox):
        score = None
        if(score_label.get() != ""):
            score = int(score_label.get())
        Exam.create(date.get() + ' ' + time.get(), name.get(), score, self.chosen_enrollee.id, self.chosen_examiner.id)
        time.delete(0, END)
        name.delete(0, END)
        score_label.delete(0, END)
        enrollee_find.delete(0, END)
        examiner_find.delete(0, END)
        self.update_all(listbox)

    def all_list_on_click(self, event):
        cs = self.all_listbox.curselection()
        self.manipulateExam(self.all_list[cs[0]])

    def find_list_on_click(self, event):
        cs = self.find_listbox.curselection()
        self.manipulateExam(self.find_list[cs[0]])

    def find_enrollee_on_click(self, event):
        cs = self.enrollee_listbox.curselection()
        self.chosen_enrollee = self.find_enrollee_list[cs[0]]
        self.chosen_enrollee_text.set(self.chosen_enrollee.to_string())

    def find_examiner_on_click(self, event):
        cs = self.examiner_listbox.curselection()
        self.chosen_examiner = self.find_examiner_list[cs[0]]
        self.chosen_examiner_text.set(self.chosen_examiner.to_string())

    def manipulateExam(self, chosenExam):
        newWindow = Toplevel(self)
        newWindow.title("New Window")
        Label(newWindow, text="Date of pass: ").grid(row=1, column=0)
        date = DateEntry(newWindow, width=12, background='darkblue', foreground='white', borderwidth=2,
                         date_pattern='dd.mm.y')
        date.grid(row=1, column=1)
        Label(newWindow, text="Time of pass(HH:MM): ").grid(row=2, column=0)
        time = Entry(newWindow, width=50)
        time.grid(row=2, column=1, columnspan=2)
        change_time = partial(self.change_time, date, time, chosenExam)
        change_time_btn = Button(newWindow, text = "Change time", command=change_time)
        change_time_btn.grid(columnspan = 3)
        if chosenExam.status == 'Planned':
            Label(newWindow, text="---------------------------------------------").grid(columnspan=3)
            Label(newWindow, text="Pass exam").grid(row=4, columnspan=3)
            Label(newWindow, text="Enter score: ").grid(row=5, column=0)
            score = Entry(newWindow, width="39")
            score.grid(row=5, column=1, columnspan=2)
            change_sal = partial(self.finish_exam, score, chosenExam)
            finish_exam_btn = Button(newWindow, text="Finish exam", command=change_sal)
            finish_exam_btn.grid(row = 6, columnspan=3)
        Label(newWindow, text="------------------------------------------------------------").grid(columnspan=3)
        delete = partial(self.delete_exam, chosenExam)
        del_btn = Button(newWindow, text="Delete exam", command=delete)
        del_btn.grid(columnspan=3)

    def change_time(self, date_entry, time_entry, chosenExam):
        chosenExam.change_time(date_entry.get() + ' ' + time_entry.get())
        self.update_all(self.all_listbox)

    def finish_exam(self, score_entry, chosenExam):
        chosenExam.finish(score_entry.get())
        self.update_all(self.all_listbox)

    def delete_exam(self, chosenExam):
        result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
        if result == 'yes':
            chosenExam.delete();
        else:
            return
        self.update_all(self.all_listbox)
