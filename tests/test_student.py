import io
import unittest
from contextlib import redirect_stdout

from student import Student


class TestStudent(unittest.TestCase):
    def test_full_name(self):
        student = Student("Харламова", "Ульяна", "ИТ", 2)
        self.assertEqual(student.full_name(), "Харламова Ульяна")

    def test_display_info_prints_card(self):
        student = Student("Харламова", "Ульяна", "ИТ", 2)
        output = io.StringIO()
        with redirect_stdout(output):
            student.display_info()
        text = output.getvalue()
        self.assertIn("ФИО:       Харламова Ульяна", text)
        self.assertIn("Факультет: ИТ", text)
        self.assertIn("Курс:      2", text)

    def test_next_course(self):
        student = Student("Иванов", "Иван", "ИТ", 5)
        student.next_course()
        self.assertEqual(student.course, 6)
        with self.assertRaises(ValueError):
            student.next_course()

    def test_wrong_course(self):
        with self.assertRaises(ValueError):
            Student("Иванов", "Иван", "ИТ", 0)

    def test_students_count(self):
        before = Student.students_count
        Student("А", "Б", "В")
        Student("Г", "Д", "Е")
        self.assertEqual(Student.students_count, before + 2)


if __name__ == "__main__":
    unittest.main()
