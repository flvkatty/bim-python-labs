import math
from typing import List
from dataclasses import dataclass


@dataclass
class Point:
    """
    Класс для хранения вещественной точки в двухмерном пространстве.
    Аттрибуты:
    x : float
        координата x
    y : float
        координата y
    """
    x: float
    y: float


def distance(a: Point, b: Point) -> float:
    """
    Расстояние между двумя точками в эвклидовом пространстве
    """
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class Polygon:
    """
    Базовый класс многоугольника
    Аттрибуты:
    points : List[Point]
        точки, описывающие многоугольнник, в порядке соединения линиями
    """

    def __init__(self, points: List[Point]):
        """
        Создание и подготовка к работе объекта "Многоугольник"
        :param points: точки, описывающие многоугольнник, в порядке соединения линиями
        """
        self._points = points

    def __str__(self) -> str:
        return "Многоугольник c точками: " + str(self._points)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(points={repr(self.points)})"

    @property
    def points(self) -> List[Point]:
        """
        Getter для аттрибута points
        :returns List[Point]: точки, описывающие многоугольнник, в порядке соединения линиями
        """
        return self._points

    def area(self) -> float:
        """
        Площадь многогольника.
        :returns float: возвращает площадь многоугольника
        """
        ...

    def perimeter(self) -> float:
        """
        Периметр многогольника
        :returns float: возвращает периметр многоугольника
        """
        result = 0.0
        for i in range(-1, len(self._points) - 1):
            a = self._points[i]
            b = self._points[i + 1]
            result += distance(a, b)
        return result


class Square(Polygon):
    """
    Квадрат, дочерний класс многоугольника
    Аттрибуты:
        length: длина стороны квадрата
    """

    def __init__(self, points: List[Point]):
        """
        Создание и подготовка к работе объекта "Квадрат"
        :param points: 4 точки, описывающие квадрат
        :raises ValueError: когда размер параметра points не равен 4
        :raises ValueError: когда длины всех сторон не равны
        """
        if len(points) != 4:
            raise ValueError("Квадрат задается 4 точками")

        length = distance(points[-1], points[0])
        for i in range(len(points) - 1):
            if distance(points[i], points[i + 1]) != length:
                raise ValueError("Длины сторон не равны")

        self.length = length
        super().__init__(points)

    def __str__(self) -> str:
        return "Квадрат c точками: " + str(self._points)

    def area(self) -> float:
        """
        Площадь квадрата.
        Вычисляется намного проще чем для произвольного многоугольника.
        :returns float: возвращает площадь многоугольника
        """
        return self.length ** 2


class Line(Polygon):
    """
    Линия, частный случай многоугольника
    Аттрибуты:
        length: длина длинии
    """

    def __init__(self, points: List[Point]):
        """
        Создание и подготовка к работе объекта "Линия"
        :param points: 2 точки, описывающие линию
        :raises ValueError: когда размер параметра points не равен 2
        """
        if len(points) != 2:
            raise ValueError("Линия задается двумя точками")

        self.length = distance(points[0], points[1])
        super().__init__(points)

    def __str__(self) -> str:
        return "Квадрат c точками: " + str(self._points)

    def area(self) -> float:
        """
        Площадь линии равняется 0.
        :returns float: возвращает 0
        """
        return 0
