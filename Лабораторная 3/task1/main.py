class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self) -> str:
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}{self.__additional_repr()})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        raise AttributeError(f"Имя книги не может быть изменено")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, name):
        raise AttributeError(f"Автор книги не может быть изменено")

    def __additional_repr(self) -> str:
        return ""


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.__name

    @pages.setter
    def pages(self, pages):
        if type(pages) != int or pages <= 0:
            raise AttributeError(f"Количество страниц должно быть целым и положительным")
        else:
            self.__pages = pages

    def __additional_repr(self) -> str:
        return f", pages={self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.__name

    @duration.setter
    def duration(self, duration):
        if type(duration) != float or duration <= 0:
            raise AttributeError(f"Продолжительность должна быть вещественным и положительным числом")
        else:
            self.__duration = duration

    def __additional_repr(self) -> str:
        return f", pages={self.__duration}"
