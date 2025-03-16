from typing import Union
import doctest


class Cake:
    """
    Документация на класс
    Класс описывает виды тортов
    """
    def __init__(self, type_of_cake: str, weight: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Торт"

        :param type_of_cake: Вид торта
        :param weight: Вес кусочка

        Примеры:
        >>> cake = Cake("Медовик", 1000)  # инициализация экземпляра класса
        """
        if not isinstance(type_of_cake, str):
            raise TypeError("Вид торта должен быть str")
        if weight <= 0:
            raise ValueError("Вес торта должен быть положительным числом")
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес торта должен быть int или float")
        self.type_of_cake = type_of_cake
        self.weight = weight

    def slicing_cake(self, pieces_num: int) -> None:
        """
        Разрезание торта на кусочки
        :param pieces_num: Количество кусков
        :raise ValueError: Если количество кусочков превышает 10, то возвращается ошибка.

        :return: Реальное количество кусков
        Примеры:
        >>> cake = Cake("Прага", 700)
        >>> cake.slicing_cake(6)
        """
        ...

    def is_bento(self) -> bool:
        """
        Проверяет является ли торт бенто_тортом (вес до 700)

        :return: Является ли торт бенто-тортом

        Примеры:
        >>> cake = Cake("Прага", 500)
        >>> cake.is_bento()
        """
        ...


class House:
    def __init__(self, floors: int, entrances_num: int):
        """
        Создание и подготовка к работе объекта "Дом"

        :param floors: Количество этажей
        :param entrances_num: Количество подъездов

        Примеры:
        >>> house = House(10, 3)
        """
        if not isinstance(floors, int):
            raise TypeError("Количество этажей должно быть int")
        if floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом")
        self.floors = floors

        if not isinstance(entrances_num, int):
            raise TypeError("Количество подъездов должно быть int")
        if entrances_num <= 0:
            raise ValueError("Количество подъездов должно быть положительным числом")
        self.entrances_num = entrances_num

    def upgrade_house(self, new_floor: int) -> None:
        """
        Надстройка новых этажей.

        :param new_floor: Количество надстроенных этажей

        Примеры:
        >>> house = House(10, 3)
        >>> house.upgrade_house(3)
        """
        if not isinstance(new_floor, int):
            raise TypeError("Надстраиваемые этажи должны быть типа int")
        if new_floor < 0:
            raise ValueError("Надстраиваемые этажи должны быть неотрицательным числом")
        ...


class Chemical_element:
    def __init__(self, proton_num: int, atomic_mass: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Химический элемент"

        :param proton_num: Количество протонов
        :param atomic_mass: Атомная масса

        Примеры:
        >>> atom = Chemical_element(3, 6.939)
        """

        if not isinstance(proton_num, int):
            raise TypeError("Количество протонов должно быть типа int")
        if proton_num <= 0:
            raise ValueError("Количество протонов должно быть положительным числом")
        self.proton_num = proton_num

        if not isinstance(atomic_mass, (int, float)):
            raise TypeError("Атомная масса должна быть int или float")
        if atomic_mass < 0:
            raise ValueError("Атомная масса должная быть положительным числом")
        self.atomic_mass = atomic_mass

    def is_isotope(self) -> bool:
        """
        Функция проверяет является ли атом изотопом

        :return: Является ли атом изотопом

        Примеры:
        >>> atom = Chemical_element(3, 6.939)
        >>> atom.is_isotope()
        """
        ...
    def nucl_sinthesis(self, num_alpha: int) -> None:
        """
        Ядерный синтез, добавление альфа-частиц
        (+2 к числу протонов и +4 к атомной массе, на каждую альфа-частицу)

        :param num_alpha: количество альфа-частиц
        :raise ValueError: Если количество количество протонов превышает существующее в таблице Менделеева
        """
        if not isinstance(num_alpha, int):
            raise TypeError("Количество альфа-частиц должно быть типа int")
        if num_alpha < 0:
            raise ValueError("Количество альфа-частиц должно быть неотрицательным")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
