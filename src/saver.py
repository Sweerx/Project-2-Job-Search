from abc import ABC, abstractmethod

class Saver(ABC):
    """Абстрактный класс для записи в файл"""

    def __init__(self, filename: str) -> None:
        """Конструктор класса"""
        self.filename = filename

    @abstractmethod
    def write_data(self, vacancies: list) -> None:
        """Абстрактный метод для записи данных"""
        pass

    @abstractmethod
    def get_data(self) -> list:
        """Абстрактный метод для получения данных"""
        pass

    @abstractmethod
    def del_data(self) -> None:
        """Абстрактный метод для удаления данных"""
        pass