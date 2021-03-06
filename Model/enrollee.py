import _sqlite3

from Model.exam import Exam

class Enrollee:
    # def __init__(self, id):
    #     self.con = _sqlite3.connect("exams.db")
    #     self.cur = self.con.cursor()
    #     self.id = id
    #     self.cur.execute("SELECT * FROM enrollee WHERE enrollee_id = ?",id)
    #     arr = self.cur.fetchall()
    #     self.surname = arr[0]["surname"]
    #     self.name = arr[0]["name"]
    #     self.patronymic = arr[0]["patronymic"]
    #     self.address = arr[0]["address"]
    #     self.birthday = arr[0]["birthday"]
    #     self.passport = arr[0]["passport"]

    @staticmethod
    def get_by_id(id):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM enrollee WHERE enrollee_id = ?",(int(id),))
        arr = cur.fetchall()
        surname = arr[0][1]
        name = arr[0][2]
        patronymic = arr[0][3]
        address = arr[0][4]
        birthday = arr[0][5]
        passport = arr[0][6]
        return Enrollee(id, surname, name, patronymic, address, birthday, passport)

    def __init__(self, id, surname, name, patronymic, address, birthday, passport):
        self.con = _sqlite3.connect("exams.db")
        self.cur = self.con.cursor()
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.birthday = birthday
        self.passport = passport

    @staticmethod
    def create(surname, name, patronymic, address, birthday, passport):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO enrollee(surname, name, patronymic, address, birthday, passport)
        VALUES(?,?,?,?,?,?)""", (surname, name, patronymic, address, birthday, passport))
        con.commit()
        cur.close()
        con.close()

    def delete(self):
        self.cur.execute("DELETE FROM enrollee WHERE enrollee_id = ?", (self.id,))
        self.cur.execute("DELETE FROM exam WHERE enrollee_id = ?", (self.id,))
        self.con.commit()

    def change_address(self, new_addr):
        self.cur.execute("""UPDATE enrollee
        SET address = ?
        WHERE enrollee_id = ?""", (new_addr, self.id))
        self.con.commit()

    def to_string(self):
        return str(self.id) + ". " + self.surname + " " + self.name + " " + self.patronymic + '; \n'\
               + self.address + '; \n' + self.birthday + '; \n' + self.passport

    @staticmethod
    def findBySurname(sur):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM enrollee WHERE surname = ?", (sur,))
        arr = cur.fetchall()
        enrollees = []
        for rec in arr:
            temp = Enrollee(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
            enrollees.append(temp)
        cur.close()
        con.close()
        return enrollees

    @staticmethod
    def all():
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM enrollee")
        arr = cur.fetchall()
        enrollees = []
        for rec in arr:
            temp = Enrollee(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
            enrollees.append(temp)
        cur.close()
        con.close()
        return enrollees

    def get_exams(self):
        self.cur.execute("SELECT * FROM exam WHERE enrollee_id = ?", (self.id,))
        arr = self.cur.fetchall()
        exams = []
        for rec in arr:
            exams.append(Exam(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6]))
        return exams

    # def __del__(self):
    #     self.cur.close()
    #     self.con.close()