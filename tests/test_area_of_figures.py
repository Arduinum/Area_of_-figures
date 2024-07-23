from unittest import TestCase, main

from area_of_figures.area_of_figures import Circle, Triangle, calculate_area


class TestAreaOfFigures(TestCase):
    """Класс для тестирования библиотеки area_of_figures"""

    def test_correct_area_circule(self):
        """Проверка на корректный расчёт площади круга"""
        
        circle = Circle(radius=7)
        circle_area = calculate_area(shape=circle)
        self.assertEqual(round(circle_area, 2), 153.94)

    def test_negative_number_area_circule(self):
        """Проверка числа на негативное при расчёте площади круга"""

        circle = Circle(radius=-7)
        circle_area = calculate_area(shape=circle)
        self.assertEqual(
            circle_area.__class__.__name__, 'NegativeNumberError'
        )

    def test_type_error_area_circule(self):
        """Проверка на ошибку типа при расчёте площади круга"""

        circle = Circle(radius=True)
        circle_area = calculate_area(shape=circle)
        self.assertEqual(
            circle_area.__class__.__name__, 'TypeError'
        )


    def test_correct_area_triangle(self):
        """Проверка на корректный расчёт площади треугольника"""

        triangle = Triangle(a=3, b=4, c=5)
        triangle_area = calculate_area(shape=triangle)
        self.assertEqual(triangle_area, 6.0)
    
    def test_negative_number_area_triangle(self):
        """
        Проверка числа на негативное при расчёте площади треугольника
        """

        triangle = Triangle(a=3, b=-4, c=5)
        triangle_area = calculate_area(shape=triangle)
        self.assertEqual(
            triangle_area.__class__.__name__, 'NegativeNumberError'
        )

    def test_type_error_area_triangle(self):
        """Проверка на ошибку типа при расчёте площади треугольника"""

        triangle = Triangle(a=3, b=None, c=5)
        triangle_area = calculate_area(shape=triangle)
        self.assertEqual(
            triangle_area.__class__.__name__, 'TypeError'
        )

    def test_is_not_triangle(self):
        """Проверка является ли фигура треугольником"""

        triangle = Triangle(a=1, b=2, c=3)
        triangle_area = calculate_area(shape=triangle)
        self.assertEqual(
            triangle_area.__class__.__name__, 'TriangleError'
        )

    def test_calculate_area_no_area(self):
        """Проверка на отсутствие метода area"""

        class TestFigure:
            """Тестовый класс фигура"""
            pass

        figure = TestFigure()
        figure_area = calculate_area(shape=figure)
        self.assertEqual(
            figure_area.__class__.__name__, 'AttributeError'
        )


if __name__ == '__main__':
    main()
