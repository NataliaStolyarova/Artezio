"""This class stores student performance data
and decides to issue a certificate."""
from random import randint


CONF = {"exam_max": 30, "lab_max": 7, "lab_num": 10, "k": 0.61}


class Student:
    """Stores learning activity data."""

    def __init__(self, name, CONF):
        self.name = name
        self.conf = CONF
        self.score = {}

    def make_lab(self, lab_points, lab_number):
        """Results of laboratory works."""
        if 0 <= lab_number <= self.conf['lab_num'] - 1:
            if lab_points > self.conf['lab_max']:
                lab_points = self.conf['lab_max']
            if lab_number not in self.score:
                self.score[lab_number] = [lab_points, 1]
                self.score[lab_number][0] = lab_points
                self.score[lab_number][1] += 1
        return self

    def make_exam(self, ex_points):
        """Result of exam passing."""
        if ex_points > self.conf['exam_max']:
            ex_points = self.conf['exam_max']
        self.score['exam'] = [ex_points]
        return self

    def is_certified(self):
        """Calculates total result and decide
        to certify student or not."""
        max_possible = self.conf['exam_max'] + \
            self.conf['lab_max'] * self.conf['lab_num']
        enough = self.conf['k'] * max_possible
        scores = [result[0] for result in self.score.values()]
        total_result = sum(scores)
        if total_result >= enough:
            return total_result, True
        return total_result, False


VASYA = Student('Vasiliy Pupkin', CONF)
for i in range(VASYA.conf['lab_num']):
    VASYA.make_lab(randint(0, VASYA.conf['lab_max']), i)
VASYA.make_exam(randint(0, VASYA.conf["exam_max"]))
print(VASYA.is_certified())
