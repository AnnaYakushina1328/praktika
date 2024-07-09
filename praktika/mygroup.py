# файл mygroup.py

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Екатерина",
        "surname": "Петрова",
        "exams": ["Физика", "Математика", "История"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Сидоров",
        "exams": ["Программирование", "Базы данных", "Алгоритмы"],
        "marks": [3, 5, 4]
    },
    {
        "name": "Ольга",
        "surname": "Козлова",
        "exams": ["Литература", "Иностранный язык", "Химия"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Сергей",
        "surname": "Кузнецов",
        "exams": ["Биология", "География", "Философия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Михайлова",
        "exams": ["Экономика", "Право", "Социология"],
        "marks": [4, 3, 4]
    }
]

'''Вам необходимо написать функцию фильтрации студентов по
средней оценке, так, чтобы на экран выводился список студентов, средний
балл которых выше заданного. Средний балл, по которому будет проводиться
фильтрация, вводится пользователем с клавиатуры'''

def filter_students_by_average_mark(students, min_average_mark):
    filtered_students = []
    for student in students:
        average_mark = sum(student["marks"]) / len(student["marks"])
        if average_mark > min_average_mark:
            filtered_students.append(student)
    return filtered_students

#использование

min_mark = float(input("Введите минимальную среднюю оценку: "))
result = filter_students_by_average_mark(groupmates, min_mark)
for student in result:
    print(f"{student['name']} {student['surname']}: {sum(student['marks']) / len(student['marks'])}")
