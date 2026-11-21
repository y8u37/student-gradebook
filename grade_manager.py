import csv
from mimetypes import init
import os


def fix_sub_name(text):
    t = text.strip()
    if not t:
        return ""
    if len(t) <= 3:
        return t.upper()
    return t.title()

class Student:
    def __init__(self, st_id, sname, mail="", subs=None):
        self.st_id = st_id.strip().upper()
        self.sname = sname.strip().title()
        self.mail = mail.strip().lower()
        self.sub_marks = {}
        if subs:
            for item in subs:
                x = fix_sub_name(item)
                if x:
                    self.sub_marks[x] = None         

def my_status(self):
        has_marks = False
        for val in self.sub_marks.values():
            if val is not None:
                has_marks = True
                break
        if not has_marks:
            return "Pending"
        a = self.calc_avg()
        if a >= 85:
            return "Distinction"
        elif a >= 75:
            return "Merit"
        elif a >= 60:
            return "Pass"
        elif a >= 50:
            return "Satisfactory"
        else:
            return "Fail"

def sub_list_text(self):
        if not self.sub_marks:
            return "None"
        lines = []
        for sub, val in self.sub_marks.items():
            if val is None:
                lines.append(f"{sub}: Pending")
            else:
                lines.append(f"{sub}: {val}")
        return "\n".join(lines)

class GradeBook:
    def __init__(self, file_name="student_gradebook.csv"):
        self.file_name = file_name
        self.records = {}
        self.read_csv()

    def ok_mail(self, mail):
        m = mail.strip()
        if "@" not in m or "." not in m:
            halves = m.split("@")
            if len(halves) != 2 or not halves[0] or "." not in halves[1]:
                return False
        return True
    
    def add_new_students(self,st_id, sname, mail, subs_raw=""):
        sid = st_id.strip().upper()
        nm = sname.strip().title()
        em = mail.strip().lower()

        if not sid:
            return False, "ID required."
        if not nm:
            return False, "Name required."
        if not self.ok_mail(em):
            return False, "Invalid email format."
        if sid in self.records:
            return False, "ID already exists."

        clean_subs = []
        for s in subs_raw.split(","):
            s = s.strip()
            if s:
                clean_subs.append(s)

            self.records[sid] = Student(sid, nm, em, clean_subs)
            self.write_csv()
            return True, "Student added."   

        def add_more_subs(self, st_id, subs_raw):
            sid = st_id.strip().upper()
            if sid not in self.records:
                return False, "Student ID not found."
            clean_subs = []
            for s in subs_raw.split(","):
                s = s.strip()
                if s:
                    clean_subs.append(s)
       
            if not clean_subs:
                return False, "Enter a subject."

            for s in clean_subs:
                self.records[sid].put_subjects(s)

            self.write_csv()
            return True, "Subjects updated."

        def give_mark(self, st_id, sub, num_text):
            sid = st_id.strip().upper()
            sb = fix_sub_name(sub)

            if sid not in self.records:
                return False, "ID not found."
            if not sb:
                return False, "Subjects required."
        
            try:
                num = float(num_text)
            except ValueError:
                return False, "Enter a valid number."
            
            if num < 0 or num > 100:
                return False, "marks must be 0-100."

            self.records[sid].put_marks(sb, num)
            self.write_csv()
            return True, "Mark saved."

    def remove_student(self, st_id):
        sid = st_id.strip().upper()
        if sid not in self.records:
            return False, "ID not found."

        self.records.pop(sid)
        self.write_csv()
        return True, "Student deleted."

    def search_and_rank(self, word=""):
        w = word.strip().lower()
        matched = []
        for st in self.records.values():
            all_sub_names = " ".join(st.sub_marks.keys()).lower()
            if (not w
                or w in st.st_id.lower()
                or w in st.sname.lower()
                or w in st.mail.lower()
                or w in all_sub_names):
                matched.append(st)

        return sorted(matched, key=lambda st: (-st.calc_avg(), st.sname))
    
             