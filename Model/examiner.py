import _sqlite3

from Model.exam import Exam

class Examiner:
    def __init__(self, id):
        self.con = _sqlite3.connect("exams.db")
        self.cur = self.con.cursor()
        self.id = id
        self.cur.execute("SELECT * FROM examiner WHERE examiner_id = ?",id)
        arr = self.cur.fetchall()
        self.surname = arr[0]["surname"]
        self.name = arr[0]["name"]
        self.patronymic = arr[0]["patronymic"]
        self.payment = arr[0]["payment"]

    def __init__(self, id, surname, name, patronymic, payment):
        self.con = _sqlite3.connect("exams.db")
        self.cur = self.con.cursor()
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.payment = payment

    @staticmethod
    def create(surname, name, patronymic, payment):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO examiner(surname, name, patronymic, payment)
        VALUES(?,?,?,?)""", (surname, name, patronymic, payment))
        con.commit()
        cur.close()
        con.close()

    def delete(self):
        self.cur.execute("DELETE FROM examiner WHERE examiner_id = ?",(self.id,))
        self.cur.execute("DELETE FROM exam  WHERE examiner_id = ?", (self.id,))
        self.con.commit()

    def change_payment(self, new_payment):
        self.cur.execute("""UPDATE examiner
        SET payment = ?
        WHERE examiner_id = ?""", (new_payment, self.id))
        self.con.commit()

    def to_string(self):
        return self.surname + " " + self.name + " " + self.patronymic + '\n' \
               + "Payment: " + str(self.payment)

    @staticmethod
    def findBySurname(sur):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM examiner WHERE surname = ?", (sur,))
        arr = cur.fetchall()
        examiners = []
        for rec in arr:
            temp = Examiner(rec[0], rec[1], rec[2], rec[3], rec[4])
            examiners.append(temp)
        cur.close()
        con.close()
        return examiners

    @staticmethod
    def all():
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM examiner")
        arr = cur.fetchall()
        examiners = []
        for rec in arr:
            temp = Examiner(rec[0], rec[1], rec[2], rec[3], rec[4])
            examiners.append(temp)
        cur.close()
        con.close()
        return examiners

    def get_exams(self):
        self.cur.execute("SELECT * FROM exam WHERE examiner_id = ?", (self.id,))
        arr = self.cur.fetchall()
        exams = []
        for rec in arr:
            exams.append(Exam(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6]))
        return exams

    def __del__(self):
        self.cur.close()
        self.con.close()