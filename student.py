"""Средняя сложность №2. Класс «Студент» с методом вывода информации."""


class Student:
    """Студент университета."""

    students_count = 0  # сколько объектов Student создано

    def __init__(self, last_name, first_name, faculty, course=1):
        if course < 1 or course > 6:
            raise ValueError("Курс должен быть от 1 до 6")
        self.last_name = last_name
        self.first_name = first_name
        self.faculty = faculty
        self.course = course
        Student.students_count += 1

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def next_course(self):
        """Перевести студента на следующий курс."""
        if self.course == 6:
            raise ValueError("Студент уже на последнем курсе")
        self.course += 1

    def display_info(self):
        """Напечатать карточку студента."""
        print("-" * 30)
        print(f"ФИО:       {self.full_name()}")
        print(f"Факультет: {self.faculty}")
        print(f"Курс:      {self.course}")
        print("-" * 30)
