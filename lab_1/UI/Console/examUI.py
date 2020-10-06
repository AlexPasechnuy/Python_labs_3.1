import datetime

from lab_1.Model.exam import Exam
from lab_1.Model.enrollee import Enrollee
from lab_1.Model.examiner import Examiner
from lab_1.UI.functions import *

def manipulate_exam(exam):
    while True:
        try:
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
        except:
            print("Error")

def all_exams():
    try:
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
    except:
        print("Error")

def find_exam():
    try:
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
    except:
        print("Error")

def add_exam():
    try:
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
    except:
        print("Error")

def exam_menu():
    while True:
        try:
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
        except:
            print("Error")

