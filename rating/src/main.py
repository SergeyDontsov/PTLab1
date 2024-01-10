import argparse
import os
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from StudentCharacteristics import StudentCharacteristics
from JSONDataReader import JSONDataReader


class DataProcessor:
    def __init__(self, data_format):
        self.data_format = data_format

    def processData(self, path):  # принимает путь к файлу
        _, file_extension = os.path.splitext(path)  # путь к файлу на базовое
        # имя и расширение.
        # Результат присваивается file_extension.
        if file_extension == ".txt":
            reader = TextDataReader()
        elif file_extension == ".json":
            reader = JSONDataReader()
        else:
            raise ValueError("Unsupported file format. Use '.txt' or '.json'.")

        students = reader.read(path)  # читаем с пути
        print("Students: ", students)

        rating = CalcRating(students).calc()  # объекту CalcRating даем
        # данные(кортеж то бишь студент: предмет-оценка)
        print("Rating: ", rating)
        
        student_char = StudentCharacteristics(students)  # instantiate StudentCharacteristics class with reader object
        
        students_with_academic_debt = student_char.count_students_with_deficits()  # calculate students with academic debt

        print("Students with academic debt: ", students_with_academic_debt)

def main():
    parser = argparse.ArgumentParser(description="Path to data file")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to data file")
    args = parser.parse_args()

    data_processor = DataProcessor(args.path)
    data_processor.processData(args.path)


if __name__ == "__main__":
    main()