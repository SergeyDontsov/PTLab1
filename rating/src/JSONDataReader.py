import json
from Types import DataType
from DataReader import DataReader

class JSONDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Открываем указанный JSON-файл для чтения
        with open(path, encoding='utf-8') as file:
            # Загружаем данные из JSON-файла
            data = json.load(file)
            # Для каждого элемента "student" в данных
            for student_data in data['students']:
                # Извлекаем имя студента
                self.key = student_data['name']
                # Создаем пустой список для предметов и оценок
                self.students[self.key] = []
                # Для каждого элемента "subject" внутри "student"
                for subject_data in student_data['subjects']:
                    # Извлекаем имя предмета
                    subj = subject_data['name']
                    # Извлекаем оценку и преобразуем в число
                    score = int(subject_data['score'])
                    # Добавляем предмет и оценку в список для студента
                    self.students[self.key].append((subj, score))
        return self.students