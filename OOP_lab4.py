class Doges:
    """Базовый класс собак на выставке"""

    def __init__(self, name: str, weight: float, age: int):
        """
        Создание и подготовка к работе объекта собака
        :param name: Название породы
        :param weight: Вес собаки
        :param age: Возраст собаки
        """
        self._name = name # Делаем атрибуты protected, чтобы занесенные данные не изменяли
        self._weight = weight
        self._age = age

    @property
    def name(self):
        """Функция использует метод getter для просмотра породы """
        return self._name

    @name.setter
    def name(self, new_name:str):
        """Функция использует метод setter для записи породы """
        if not isinstance(new_name, str):
            raise TypeError('Название породы должно быть типа str')
        self._name = new_name

    @property
    def weight(self):
        """Функция использует метод getter для просмотра веса """
        return self._weight

    @weight.setter
    def weight(self, new_weight: float):
        """Функция использует метод setter для записи веса"""
        if not isinstance(new_weight, float):
            raise TypeError("Вес должен быть типа float")
        if new_weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self._weight = new_weight

    @property
    def age(self):
        """Функция использует метод getter для просмотра возраста"""
        return self._age

    @age.setter
    def weight(self, new_age: int):
        """Функция использует метод setter для записи возраста"""
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен быть типа int")
        if new_age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self._age = new_age

    def is_dog_fat(self) -> str:
        """
        Функция проверяет проходит ли собака
        по критерию максимального веса 100кг
        """
        if self._weight > 100:
            return "Собачки слишком много :("
        return f"Собачка проходит по весу!"

    def age_category(self) -> str:
        """
        Функция распределяет собак на две категории:
        щенков и взрослых
        """
        if self._age < 2: #Если возраст больше 2 лет - взрослый, меньше - щенок
            return "Категория: щенки"
        return "Категория: взрослые"

    def __str__(self) -> str:
        return f"Вес собаки породы {self.name} - {self.weight} кг."


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r})"

class Hounds(Doges):
    """Класс гончих собак, наследованный от базового класса Doges"""
    def __init__(self, name: str, weight: float, age: int, ear_length: int):
        """
        Создание и подготовка к работе объекта гончая собака
        :param name: Название породы
        :param weight: Вес собаки
        :param age: Возраст собаки
        :param ear_length: Длина ушей
        """
        super().__init__(name, weight, age) #Вызываем конструктор базового класса
        self._ear_length = ear_length

    @property
    def ear_length(self):
        """Функция использует метод getter для просмотра длины ушей"""
        return self._ear_length

    @ear_length.setter
    def ear_length(self, new_length):
        """Функция использует метод setter для записи длины ушей"""
        if not isinstance(new_length, int):
            raise TypeError("Длина ушей должна быть типа int")
        if new_length <= 0:
            raise ValueError("Длина ушей должна быть положительным числом")
        self._weight = new_weight

    def is_dog_fat(self) -> str:
        """
        Перегрузка метода родительского класса
        из-за более строгих требований к гончим
        """
        if self._weight > 50:
            return "Собачки слишком много :("
        return f"Собачка проходит по весу!"

    # Метод age_category наследован из родительского класса

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r},\
         weight={self.weight!r}, ear_length={self.ear_length!r})"


if __name__ == "__main__":
    sharik = Doges("pudel", 12, 1)
    print(sharik.age_category())
    print(sharik.is_dog_fat())
    tuzik = Hounds("borzaya", 55, 5, 30)
    print(tuzik.age_category())
    print(tuzik.is_dog_fat())