# https://quera.org/problemset/16397

import operator as op


class Grade:
    def __init__(self, student_id, course_code, score):
        self.student_id = int(student_id)
        self.course_code = int(course_code)
        self.score = float(score)

    @classmethod
    def parse(cls, clause):
        return cls(*str(clause).split())

    def __str__(self):
        return f"{self.student_id} {self.course_code} {self.score}"


class CourseUtil:
    def __init__(self):
        self.path = None
        self.grades = []

    def set_file(self, path):
        self.path = path
        with open(self.path) as handler:
            self.grades = list(map(Grade.parse, filter(bool, handler.readlines())))

    def load(self, idx):
        if idx <= self.count():
            return self.grades[idx-1]

    def calc_student_average(self, student_id):
        if self.grades:
            grades = list(filter(lambda g: g.student_id == student_id, self.grades))
            return sum(map(op.attrgetter('score'), grades)) / len(grades)

    def calc_course_average(self, code):
        if self.grades:
            grades = list(filter(lambda g: g.course_code == code, self.grades))
            return sum(map(op.attrgetter('score'), grades)) / len(grades)

    def count(self):
        return len(self.grades)

    def save(self, grade):
        if self.path is None:
            return

        features = op.attrgetter('student_id', 'course_code')
        if features(grade) in list(map(features, self.grades)):
            return

        self.grades.append(grade)
        self.rewrite()

    def rewrite(self):
        if self.path:
            self.duplicate(self.path)

    def duplicate(self, new_path):
        with open(new_path, 'wt') as handler:
            handler.write('\n'.join(map(str, self.grades)))
