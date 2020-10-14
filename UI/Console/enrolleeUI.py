from datetime import datetime

from Model.enrollee import Enrollee
from UI.functions import *

def manipulate_enrollee(enrollee):
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. See exams")
            print("2. Change address")
            print("3. Delete enrollee")
            res = int(input("What do you want to do?( -1 to go back): "))
            if res == 1:
                print_arr(enrollee.get_exams())
            elif res == 2:
                new_addr = input("Enter new address: ")
                enrollee.change_address(new_addr)
            elif res == 3:
                enrollee.delete()
                del enrollee
                print("Enrollee deleted")
                return
            elif res == -1:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")

def all_enrollees():
    try:
        enrollees = Enrollee.all()
        print_arr(enrollees)
        if len(enrollees) == 0:
            print("No results")
        else:
            res = int(input("Enter number of selected enrollee or '-1' to go back: "))
            if res > 0 and res <= len(enrollees):
                manipulate_enrollee(enrollees[res - 1])
                return
            if res == -1:
                return
            else:
                print("Incorrect input")
    except:
        print("Error")

def find_enrollee():
    try:
        sur = input("Enter surname to search: ")
        enrollees = Enrollee.findBySurname(sur)
        print_arr(enrollees)
        if len(enrollees) == 0:
            print("No results")
        else:
            res = int(input("Enter number of selected enrollee or '-1' to go back: "))
            if res > 0 and res <= len(enrollees):
                manipulate_enrollee(enrollees[res - 1])
                return
            elif res == -1:
                return
            else:
                print("Incorrect input")
    except:
        print("Error")

def add_enrollee():
    try:
        surname = input("Enter surname: ")
        name = input("Enter name: ")
        patronymic = input("Enter patronymic: ")
        address = input("Enter address: ")
        birthday = datetime.strptime(input("Enter date of birthday(DD.MM.YYYY): "), '%d.%m.%Y').date().strftime('%d.%m.%Y')
        passport = input("Enter number of passport: ")
        Enrollee.create(surname, name, patronymic, address, birthday, passport)
    except:
        print("Error")

def enrollee_menu():
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. See all")
            print("2. Find")
            print("3. Add new")
            res = int(input("What do you want to do?( -1 to go back): "))
            if res == 1:
                all_enrollees()
            elif res == 2:
                find_enrollee()
            elif res == 3:
                add_enrollee()
            elif res == -1:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")

