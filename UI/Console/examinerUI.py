from lab_1.Model.examiner import Examiner
from lab_1.UI.functions import *

def manipulate_examiner(examiner):
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. See exams")
            print("2. Change payment")
            print("3. Delete examiner")
            res = int(input("What do you want to do?( -1 to go back): "))
            if res == 1:
                print_arr(examiner.get_exams())
            elif res == 2:
                new_pay = int(input("Enter new payment: "))
                examiner.change_payment(new_pay)
            elif res == 3:
                examiner.delete()
                del examiner
                return
            elif res ==-1:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")

def all_examiners():
    try:
        examiners = Examiner.all()
        print_arr(examiners)
        if len(examiners) == 0:
            print("No results")
        else:
            res = int(input("Enter number of selected examiner or '-1' to go back: "))
            if res > 0 and res <= len(examiners):
                manipulate_examiner(examiners[res - 1])
            elif res == -1:
                return
            else:
                print("Incorrect input")
    except:
        print("Error")

def find_examiner():
    try:
        sur = input("Enter surname to search: ")
        examiners = Examiner.findBySurname(sur)
        print_arr(examiners)
        if len(examiners) == 0:
            print("No results")
        else:
            res = int(input("Enter number of selected examiner or '-1' to go back: "))
            if res > 0 and res <= len(examiners):
                manipulate_examiner(examiners[res - 1])
            elif res == -1:
                return
            else:
                print("Incorrect input")
    except:
        print("Error")

def add_examiner():
    try:
        surname = input("Enter surname: ")
        name = input("Enter name: ")
        patronymic = input("Enter patronymic: ")
        payment = int(input("Enter payment: "))
        Examiner.create(surname, name, patronymic, payment)
    except:
        print("Error")

def examiner_menu():
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. See all")
            print("2. Find")
            print("3. Add new")
            res = int(input("What do you want to do?( -1 to go back): "))
            if res == 1:
                all_examiners()
            elif res == 2:
                find_examiner()
            elif res == 3:
                add_examiner()
            elif res == -1:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")
