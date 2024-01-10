from CalcRating import RatingType
import numpy as np
from typing import List

class StudentCharacteristics:
    def __init__(self, students):
        self.students = students

    def count_students_with_deficits(self):
        count = 0
        for student, marks in self.students.items():
           for subject, mark in marks:
              if mark < 61:
                 count += 1
                 break
        return count