import _sqlite3

class Exam:
    def __init__(self, id, pass_time, exam_name, score, status, enrollee_id, examiner_id):
        self.con = _sqlite3.connect("exams.db")
        self.cur = self.con.cursor()
        self.id = id
        self.pass_time = pass_time
        self.exam_name = exam_name
        self.score = score
        self.status = status
        self.enrollee_id = enrollee_id
        self.examiner_id = examiner_id

    @staticmethod
    def get_by_id(id):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM exam WHERE exam_id = ?", (id,))
        arr = cur.fetchall()
        pass_time = arr[0][1]
        exam_name = arr[0][2]
        score = arr[0][3]
        status = arr[0][4]
        enrollee_id = arr[0][5]
        examiner_id = arr[0][6]
        return Exam(id, pass_time, exam_name, score, status, enrollee_id, examiner_id)

    @staticmethod
    def create(pass_time , exam_name , score, enrollee_id , examiner_id):
        status = "Passed"
        if score == None:
            status = "Planned"
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO exam(pass_time, exam_name, score, status, enrollee_id, examiner_id)
        VALUES(?,?,?,?,?,?)""", (pass_time, exam_name, score, status, enrollee_id, examiner_id))
        con.commit()
        cur.close()
        con.close()

    def delete(self):
        self.cur.execute("DELETE FROM exam WHERE exam_id = ?", (self.id,))
        self.con.commit()

    def finish(self, score):
        self.cur.execute("""UPDATE exam
        SET status = "PASSED",
            score = ?
        WHERE exam_id = ?""", (score, self.id))
        self.con.commit()

    def change_time(self, new_time):
        self.cur.execute("""UPDATE exam
        SET pass_time = ?
        WHERE exam_id = ?""", (new_time, self.id))
        self.con.commit()

    def to_string(self):
        res = str(self.id) + ". " + self.exam_name + "; " + self.pass_time + "; "
        res += self.status + "; "
        if self.status == "PASSED":
            res += str(self.score) + ' points; '
        self.cur.execute("SELECT surname, name, patronymic FROM enrollee WHERE enrollee_id = ?", (self.enrollee_id,))
        arr = self.cur.fetchall()
        res += "\n Enrollee: " + arr[0][0] + " " + arr[0][1] + " " + arr[0][2] + '; \n'
        self.cur.execute("SELECT surname, name, patronymic FROM examiner WHERE examiner_id = ?", (self.examiner_id,))
        arr = self.cur.fetchall()
        res += "Examiner: " + arr[0][0] + " " + arr[0][1] + " " + arr[0][2]
        return res

    def get_enrollee(self):
        self.cur.execute("SELECT surname, name, patronymic FROM enrollee WHERE enrollee_id = ?", (self.enrollee_id,))
        arr = self.cur.fetchall()
        return arr[0][0] + " " + arr[0][1] + " " + arr[0][2]

    def get_examiner(self):
        self.cur.execute("SELECT surname, name, patronymic FROM examiner WHERE examiner_id = ?", (self.examiner_id,))
        arr = self.cur.fetchall()
        return arr[0][0] + " " + arr[0][1] + " " + arr[0][2]

    @staticmethod
    def all():
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM exam")
        arr = cur.fetchall()
        exams = []
        for rec in arr:
            temp = Exam(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
            exams.append(temp)
        cur.close()
        con.close()
        return exams

    @staticmethod
    def find_by_date(date):
        con = _sqlite3.connect("exams.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM exam WHERE pass_time LIKE ?", (date + '%',))
        arr = cur.fetchall()
        exams = []
        for rec in arr:
            temp = Exam(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6])
            exams.append(temp)
        cur.close()
        con.close()
        return exams

    def __del__(self):
        self.cur.close()
        self.con.close()