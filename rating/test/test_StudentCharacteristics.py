import pytest
import sys
sys.path.append('C:/Users/Asus/rating/rating/src')
from StudentCharacteristics import StudentCharacteristics
import unittest
import json
from typing import Dict, Any


# Модульные тесты для класса StudentCharacteristics
class TestStudentCharacteristics(unittest.TestCase):
    def setUp(self):
        self.data = {
            "students": [
                {
                    "name": "John",
                    "scores": {"math": 70, "english": 55}
                },
                {
                    "name": "Jane",
                    "scores": {"math": 45, "english": 80}
                }
            ]
        }
        self.characteristics = StudentCharacteristics(self.data)

    def test_calculate_students_with_academic_debt(self):
        self.assertEqual(self.characteristics.calculate_students_with_academic_debt(), 2)
    
    def test_calculate_students_with_no_academic_debt(self):
        data = {
            "students": [
                {
                    "name": "Bob",
                    "scores": {"math": 80, "english": 75}
                }
            ]
        }
        characteristics = StudentCharacteristics(data)
        self.assertEqual(characteristics.calculate_students_with_academic_debt(), 0)

if __name__ == '__main__':
    unittest.main()