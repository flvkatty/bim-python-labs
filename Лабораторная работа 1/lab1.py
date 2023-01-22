import doctest
from typing import List, Tuple

class Counter:
    def __init__(self, initial_value: int, max_value: int):
        """
        Создание и подготовка к работе объекта "Счетчик"
        :param initial_value: Изначальное значение счетчика
        :param max_value: Максимальное значение счетчика
        Примеры:
        >>> counter0 = Counter(0, 10)
        >>> counter10 = Counter(10, 100)
        >>> neg_counter = Counter(-5, 0)
        """
        if not isinstance(initial_value, int) or not isinstance(max_value, int):
            raise TypeError("Изначальное и максимальное значение счетчиков должны быть целымы числами типа int")
        if initial_value > max_value:
            raise ValueError("Максимально значение должно быть не меньше чем начальное")
        self.value = initial_value
        self.max_value = max_value

    """
    Возвращает текущее значение счетчика
    
    :return: Текущее значение счетчикаю
    
    Примеры:
    >>> Counter(0, 10).get()
    0
    >>> Counter(-50, 0).get()
    -50
    """
    def get(self) -> int:
        ...

    """
    Прибавляет достиг ли счетчик максимального значения
    
    :return: Достиг ли счетчик максимального значения
    
    Примеры:
    >>> counter = Counter(0, 2)
    >>> counter.add(2)
    >>> counter.is_max()
    True
    >>> counter2 = Counter(0, 10)
    >>> counter2.is_max()
    False
    """
    def is_max(self) -> bool:
        ...

    """
    Прибавляет к счетчику число
    :param amount: число, на которое будет увеличен счетчик
    Примеры:
    >>> counter = Counter(0, 100)
    >>> counter.add(10)
    >>> counter.add(5)
    >>> counter.get()
    15
    >> counter2 = Counte(0, 10)
    >> counter2.add(100)
    >> counter2.get()
    10
    """
    def add(self, amount: int) -> None:
        ...

    """
    Прибавляет к счетчику единицу
    Примеры:
    >>> counter = Counter(0, 2)
    >>> counter.increment()
    >>> counter.get()
    Лабораторная работа 1
    >>> counter.increment()
    >>> counter.get()
    2
    >>> counter.increment()
    >>> counter.get()
    2
    """
    def increment(self) -> None:
        ...


class CombinationLock:
    def __init__(self, combination: int, is_open: bool):
        """
        Создание и подготовка к работе объекта "Кодовый замок"
        :param combination: Изначальная комбинация на замкп
        :param is_open: Отркыт ли замок изначально
        Примеры:
        >>> lock = CombinationLock(0, False)
        >>> lock666 = CombinationLock(666, True)
        """
        if not isinstance(combination, int):
            raise TypeError("Комбинация должна быть целым числом типа int")
        elif not isinstance(is_open, bool):
            raise TypeError("is_open должен типом bool")

        if not 0 <= combination <= 999:
            raise ValueError("Комбинация должна быть в диапазаоне от 0 до 999")
        self.combination = combination
        self.is_open = is_open

    """
    Проверяет открыт ли замок

    :return: открыт ли замок

    Примеры:
    >>> CoombinationLock(0, False).is_open()
    False
    >>> CoombinationLock(0, True).is_open()
    True
    """
    def is_open(self) -> bool:
        ...

    """
    Меняет комбинацию на замке на новую

    :param old_combination: Старая комбинация
    :param new_combination: Новая комбинация
    :return: Удалось ли сменить комбинацию

    Примеры:
    >>> lock = CoombinationLock(245, True)
    >>> lock.reset_combination(111, 3)
    False
    >>> lock.reset_combination(245, 666)
    True
    """
    def reset_combination(self, old_combination: int, new_combination: int) -> bool:
        ...

    """
    Отрыть замок

    :param combination: Комбинация для отрытия замка
    :return: Удалось ли открыть

    Примеры:
    >>> lock = CoombinationLock(245, True)
    >>> lock.unlock(245)
    True
    """
    def unlock(self, combination: int) -> bool:
        ...

    """
    Закрыть замок

    Примеры:
    >>> lock = CoombinationLock(245, False)
    >>> lock.lock()
    """
    def lock(self) -> None:
        ...

class LCDScreen:
    def __init__(self, width: int, height: int):
        """
        Создание и подготовка к работе объекта "ЖК экран"
        :param width: Ширина в пиксилях
        :param height: Высота в пиксилях
        Примеры:
        >>> lcd = LCDScreen(1920, 1080)
        >>> lcd100 = LCDScreen(100, 100)
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Высота и ширина должны быть целымы числами типа int")

        if width <= 0 or height <= 0:
            raise ValueError("Высота и ширина должны быть положительными")

        self.width = width
        self.height = height
        self.is_on = False

    """
    Изобразить на дисплее

    :param picture: Значения всех пикселей в RGB формате.
    :return: Удалось ли открыть

    Примеры:
    >>> lcd = LCDScreen(Лабораторная работа 1, 2)
    >>> lcd.draw([[23, 53, 255], [12, 23, 123]])
    """
    def draw(self, picture: List[List[Tuple[int, int, int]]]) -> None:
        ...

    """
    Проверяет включен ли дисплей

    :return: Включен ли дисплей

    Примеры:
    >>> lcd = LCDScreen(Лабораторная работа 1, 2)
    >>> lcd.is_on()
    False
    """
    def is_on(self) -> bool:
        ...

    """
    Нажимает на кнопку питания. Включает или выключает дисплей.
 
    Примеры:
    >>> lcd = LCDScreen(Лабораторная работа 1, 2)
    >>> lcd.press_power_button()
    """
    def press_power_button(self) -> None:
        ...


if __name__ == "__main__":
    doctest.testmod()
