from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float

    def display_info(self):
        return print(f'name: {self.name}, age: {self.age}, major: {self.major}, gpa: {self.gpa}')

    def calculate_grade(self):
        if self.gpa == 5:
            return 'Отлично'
        elif self.gpa >= 3.5:
            return 'Хорошо'
        elif 2 < self.gpa < 3.5:
            return 'Удовлетворительно'
        elif self.gpa == 2:
            return 'Неудовлетворительно'

students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
]

students_sorted = sorted(students, key=lambda student: student.gpa, reverse=True)

# Отображение информации о студентах
for student in students_sorted:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")