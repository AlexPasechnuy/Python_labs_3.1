from lab_1.UI.Console.enrolleeUI import *
from lab_1.UI.Console.examinerUI import *
from lab_1.UI.Console.examUI import *

def main_menu():
    while True:
        try:
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
        except:
            print("Error")

main_menu()
