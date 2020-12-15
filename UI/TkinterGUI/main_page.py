from tkinter import *
from tkinter.ttk import Notebook

from UI.TkinterGUI.enrolleeGUI import EnrolleePage
from UI.TkinterGUI.examinerGUI import ExaminerPage
from UI.TkinterGUI.examGUI import ExamPage

if __name__ == "__main__":
    root = Tk()
    root.update()
    tab_control = Notebook(root)
    p1 = EnrolleePage()
    p2 = ExaminerPage()
    p3 = ExamPage()
    tab_control.add(p1, text = "Enrollee")
    tab_control.add(p2, text="Examiner")
    tab_control.add(p3, text="Exam")
    tab_control.pack(expand=1, fill='both')
    root.state('zoomed')
    root.mainloop()