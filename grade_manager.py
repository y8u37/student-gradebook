import csv
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