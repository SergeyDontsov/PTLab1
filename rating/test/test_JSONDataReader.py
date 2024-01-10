import unittest
import sys
sys.path.append('C:/Users/Asus/rating/rating/src')
from JSONDataReader import JSONDataReader
import json
import os

class JSONDataReaderTestCase(unittest.TestCase):
     def setUp(self):
       self.reader = JSONDataReader()

     def test_read(self):
       data = {
        "students": [
            {
                "name": "John Doe",
                "subjects": [
                    {"name": "Math", "score": "90"},
                    {"name": "Science", "score": "85"}
                ]
            },
            {
                "name": "Jane Smith",
                "subjects": [
                    {"name": "English", "score": "95"},
                    {"name": "History", "score": "80"}
                ]
            }
        ]
    }
       json_data = json.dumps(data)

       # Create a temporary JSON file
       with open('test.json', 'w') as file:
           file.write(json_data)

    # Read the JSON file using the JSONDataReader class
       result = self.reader.read('test.json')

    # Check if the data is correctly read and stored
       self.assertEqual(result, {
          "John Doe": [("Math", 90), ("Science", 85)],
          "Jane Smith": [("English", 95), ("History", 80)]
       })

    # Delete the temporary JSON file
       os.remove('test.json')

class JSONDataReaderTest(unittest.TestCase):
    def test_read(self):
        reader = JSONDataReader()
        data = reader.read("test_data.json")
        
        # Проверка, что данные были успешно прочитаны
        self.assertIsInstance(data, dict)
        
        # Проверка, что все студенты были добавлены
        self.assertEqual(len(data.keys()), 3)
        
        # Проверка, что у каждого студента есть список предметов и оценок
        for student in data.values():
            self.assertIsInstance(student, list)
            self.assertTrue(all(isinstance(subj, tuple) for subj in student))
        
        # Проверка, что все предметы были добавлены и соответствуют ожидаемым значениям
        expected_subjects = ['математика', 'литература', 'программирование']
        for student in data.values():
            subjects = [subj[0] for subj in student]  # Извлекаем только названия предметов
            self.assertCountEqual(subjects, expected_subjects)
        
        # Проверка, что все оценки были добавлены и соответствуют ожидаемым значениям
        expected_scores = [67, 100, 91]
        for student in data.values():
            scores = [subj[1] for subj in student]  # Извлекаем только оценки
            self.assertCountEqual(scores, expected_scores)


if __name__ == '__main__':
    unittest.main()
