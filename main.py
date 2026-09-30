"""Лабораторная работа №3, вариант 2 — демонстрация классов."""

from factory import ShapeFactory
from shape_list import ShapeList
from student import Student
from vector import Vector


def main():
    print("1) Класс Student")
    student = Student("Харламова", "Ульяна", "Информационные технологии", 2)
    student.display_info()
    student.next_course()
    print(f"После перевода: {student.course} курс")

    print("\n2) Фигуры, созданные фабрикой")
    descriptions = [
        "circle 1.5", "rectangle 3 4", "square 2", "triangle 3 4 5",
    ]
    shapes = ShapeList(ShapeFactory.from_string(d) for d in descriptions)
    for shape in shapes:
        print("  " + shape.describe())

    print("\n3) ShapeList — список фигур с дополнительными методами")
    print(f"  Общая площадь: {shapes.total_area():.2f}")
    print(f"  Самая большая: {shapes.largest().describe()}")
    print(f"  По возрастанию площади: {shapes.sorted_by_area()}")
    try:
        shapes.append("не фигура")
    except TypeError as error:
        print(f"  Ошибка: {error}")

    print("\n4) Перегрузка оператора +")
    a = Vector(1, 2)
    b = Vector(3, -1)
    print(f"  {a} + {b} = {a + b}")
    print(f"  Сумма трёх векторов: {sum([a, b, Vector(0, 5)])}")
    print(f"  Длина {a + b}: {abs(a + b):.3f}")


if __name__ == "__main__":
    main()
