# import tkinter
# #
# # top = tkinter.Tk()
# # text = tkinter.Label(top, text = "Select type to work with")
# # enrollee = tkinter.Button(top,text="Enrollee",
# #                       command=top.quit)
# # examiner = tkinter.Button(top,text="Examiner",
# #                       command=top.quit)
# # exam = tkinter.Button(top,text="Exam",
# #                       command=top.quit)
# # text.pack()
# # enrollee.pack()
# # examiner.pack()
# # exam.pack()
# # tkinter.mainloop()

from tkinter import *
from tkinter.ttk import Notebook

from UI.GUI.enrolleeGUI import Enrollee
from UI.GUI.examinerGUI import Examiner
from UI.GUI.examGUI import Exam

if __name__ == "__main__":
    root = Tk()
    root.update()
    tab_control = Notebook(root)
    p1 = Enrollee()
    p2 = Examiner()
    p3 = Exam()
    tab_control.add(p1, text = "Enrollee")
    tab_control.add(p2, text="Examiner")
    tab_control.add(p3, text="Exam")
    tab_control.pack(expand=1, fill='both')
    root.state('zoomed')
    root.mainloop()