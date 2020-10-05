import _sqlite3
from datetime import datetime

from lab_1.enrollee import Enrollee
from lab_1.examiner import Examiner
from lab_1.exam import Exam

#works
def print_arr(arr):
    number = 1
    for rec in arr:
        print(number, ". ", rec.to_string())
        number+=1

############################################################################
#works
def manipulate_enrollee(enrollee):
    while True:
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
            return
        elif res ==-1:
            return
        else:
            print("Incorrect input")

#works
def all_enrollees():
    enrollees = Enrollee.all()
    print_arr(enrollees)
    if len(enrollees) == 0:
        print("No results")
    else:
        res = int(input("Enter number of selected enrollee or '-1' to go back: "))
        if res > 0 and res <= len(enrollees):
            manipulate_enrollee(enrollees[res - 1])
        if res == -1:
            return
        else:
            print("Incorrect input")

#works
def find_enrollee():
    sur = input("Enter surname to search: ")
    enrollees = Enrollee.findBySurname(sur)
    print_arr(enrollees)
    if len(enrollees) == 0:
        print("No results")
    else:
        res = int(input("Enter number of selected enrollee or '-1' to go back: "))
        if res > 0 and res <= len(enrollees):
            manipulate_enrollee(enrollees[res - 1])
        elif res == -1:
            return
        else:
            print("Incorrect input")

#works
def add_enrollee():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    patronymic = input("Enter patronymic: ")
    address = input("Enter address: ")
    birthday = datetime.strptime(input("Enter date of birthday(DD.MM.YYYY): "), '%d.%m.%Y').date().strftime('%d.%m.%Y')
    passport = input("Enter number of passport: ")
    Enrollee.create(surname, name, patronymic, address, birthday, passport)

#works
def enrollee_menu():
    while True:
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


################################################################################
# works
def manipulate_examiner(examiner):
    while True:
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

#works
def all_examiners():
    cur.execute("SELECT * FROM examiner")
    arr = cur.fetchall()
    examiners = Examiner.all()
    print_arr(examiners)
    if len(examiners) == 0:
        print("No results")
    else:
        res = int(input("Enter number of selected examiner or '-1' to go back: "))
        if res > 0 and res <= len(arr):
            manipulate_examiner(examiners[res - 1])
        elif res == -1:
            return
        else:
            print("Incorrect input")

#works
def find_examiner():
    sur = input("Enter surname to search: ")
    cur.execute("SELECT * FROM examiner WHERE surname = ?", (sur,))
    arr = cur.fetchall()
    examiners = Examiner.findBySurname(sur)
    print_arr(examiners)
    if len(examiners) == 0:
        print("No results")
    else:
        res = int(input("Enter number of selected examiner or '-1' to go back: "))
        if res > 0 and res <= len(arr):
            manipulate_examiner(examiners[res - 1])
        elif res == -1:
            return
        else:
            print("Incorrect input")

#works
def add_examiner():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    patronymic = input("Enter patronymic: ")
    payment = int(input("Enter payment: "))
    Examiner.create(surname, name, patronymic, payment)

#works
def examiner_menu():
    while True:
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


#################################################################################

def manipulate_exam(exam):
    while True:
        print("___________________________________________________________________________\n")
        print("1. Change time")
        print("2. Finish exam")
        print("3. Delete exam")
        res = int(input("What do you want to do?( -1 to go back): "))
        if res == 1:
            new_time = datetime.strptime(input("Enter new time of pass(DD.MM.YYYY HH:MM): "), '%d.%m.%Y %H:%M').strftime('%d.%m.%Y %H:%M')
            exam.change_time(new_time)
        elif res == 2:
            exam.finish(int(input("Enter score of exam: ")))
        elif res == 3:
            exam.delete()
            del exam
            return
        elif res ==-1:
            return
        else:
            print("Incorrect input")

def all_exams():
    exams = Exam.all()
    print_arr(exams)
    if len(exams) == 0:
        print("No results")
    else:
        res = int(input("Enter number of selected exam or '-1' to go back: "))
        if res > 0 and res <= len(exams):
            manipulate_exam(exams[res - 1])
        elif res == -1:
            return
        else:
            print("Incorrect input")

def find_exam():
    date = input("Enter date of exam: ")
    exams = Exam.find_by_date(date)
    print_arr(exams)
    if len(exams) == 0:
        print("No results")
    else:
        res = int(input("Enter number of selected exam or '-1' to go back: "))
        if res > 0 and res <= len(exams):
            manipulate_exam(exams[res - 1])
        elif res == -1:
            return
        else:
            print("Incorrect input")

def add_exam():
    pass_time = datetime.strptime(input("Enter time of pass(DD.MM.YYYY HH:MM): "), '%d.%m.%Y %H:%M').strftime('%d.%m.%Y %H:%M')
    exam_name = input("Enter name of exam: ")
    status = "PLANNED"
    score = input("Enter score of exam: ")
    enrollee_id = 0
    examiner_id = 0
    if score == "":
        score = None
    else:
        score = int(score)
        status = "PASSED"
    while True:                         #select enrollee by surname
        enrollee_surn = input("Enter surname of enrollee: ")
        if enrollee_surn == "-1":
            return
        enrollees = Enrollee.findBySurname(enrollee_surn)
        if len(enrollees) == 0:
            print("No results. Enter '-1' to stop adding exam ornew surname to try again: ")
        else:
            print_arr(enrollees)
            user_input = int(input("Enter number of selected enrollee, or '-1' to stop adding exam: "))
            if user_input >= 0 or user_input < len(enrollees):
                enrollee_id = user_input
                break
            elif user_input == -1:
                return
            else:
                print("Incorrect input")
    while True:                         #select examiner by surname
        examiner_surn = input("Enter surname of examiner: ")
        if examiner_surn == "-1":
            return
        examiners = Examiner.findBySurname(examiner_surn)
        if len(examiners) == 0:
            print("No results. Enter '-1' to stop adding exam or new surname to try again: ")
        else:
            print_arr(examiners)
            user_input = int(input("Enter number of selected examiner, or '-1' to stop adding exam: "))
            if user_input >= 0 or user_input < len(examiners):
                examiner_id = user_input
                break
            elif user_input == -1:
                return
            else:
                print("Incorrect input")
    Exam.create(pass_time, exam_name, score, status, enrollee_id, examiner_id)

def exam_menu():
    while True:
        print("___________________________________________________________________________\n")
        print("1. See all")
        print("2. Find by time")
        print("3. Add new")
        res = int(input("What do you want to do?( -1 to go back): "))
        if res == 1:
            all_exams()
        elif res == 2:
            find_exam()
        elif res == 3:
            add_exam()
        elif res ==-1:
            return
        else:
            print("Incorrect input")


#################################################################################

def main_menu():
    while True:
        print("___________________________________________________________________________\n")
        print("1. Enrollee")
        print("2. Examiner")
        print("3. Exam")
        res = int(input("Select type to work with( -1 to go back): "))
        if res == 1:
            enrollee_menu()
        elif res == 2:
            examiner_menu()
        elif res == 3:
            exam_menu()
        elif res ==-1:
            return
        else:
            print("Incorrect input")

con = _sqlite3.connect("exams.db")
cur = con.cursor()
main_menu()
cur.close()
con.close()
