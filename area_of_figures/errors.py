class NegativeNumberError(Exception):
    """Класс ошибка отрицательное число"""
    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
