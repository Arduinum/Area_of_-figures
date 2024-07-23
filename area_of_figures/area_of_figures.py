from math import sqrt, pi
from abc import abstractmethod, ABC

from errors import NegativeNumberError


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

        # проверяем является ли фигура треугольником
        if s > max([self.a, self.b, self.c]) / 2:
            # вычисляем площадь треугольника по формуле Герона
            return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        else:
            raise ValueError(
                "Сумма длин сторон должна быть больше полупериметра!"
            )


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
    except AttributeError as err:
        return err
    except ValueError as err:
        return err
    except TypeError as err:
        return err
    except NegativeNumberError as err:
        return err


if __name__ == '__main__':
    circule = Circle(radius=-1)
    circule_area = calculate_area(shape=circule)
    print(f'Площадь круга = {circule_area}')

    triangle = Triangle(a=3, b=4, c=5)
    triangle_area = calculate_area(shape=triangle)
    print(f'Площадь треугольника = {triangle_area}')
