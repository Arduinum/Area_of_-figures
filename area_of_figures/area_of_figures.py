from math import sqrt, pi
from abc import abstractmethod, ABC

from area_of_figures.errors import NegativeNumberError, TriangleError


class Figure(ABC):
    """Абстрактный класс для фигуры"""

    @abstractmethod
    def area():
        """Абстрактный метод для рассчёта площади фигуры"""
        pass


class Circle(Figure):
    """Класс для фигуры круг"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Метод для рассчёта площади круга"""
        
        return self.radius ** 2 * pi


class Triangle(Figure):
    """Класс для фигуры треугольник"""
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # вычисляем полупериметр
        s = (self.a + self.b + self.c) / 2

        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            raise TriangleError('Стороны не могут образовать треугольник!')
        # вычисляем площадь треугольника по формуле Герона
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def calculate_area(shape):
    """Функция для рассчёта площади фигур"""
    
    try:
        for value in shape.__dict__.values():
            if str(type(value)) not in ("<class 'int'>", "<class 'float'>"):
                raise TypeError('Тип данных может быть лишь int или float!')
            
            if value <= 0:
                raise NegativeNumberError(
                    'Введённое число не может быть отрицательным или нолём!'
                )
             
        return shape.area()
    except (
        AttributeError, 
        ValueError, 
        TypeError, 
        NegativeNumberError, 
        TriangleError
        ) as err:
        return err
