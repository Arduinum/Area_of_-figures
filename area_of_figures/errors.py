class NegativeNumberError(Exception):
    """Класс ошибка отрицательное число"""
    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value


class TriangleError(Exception):
    """Класс ошибка фигуры не треугольник"""
    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
