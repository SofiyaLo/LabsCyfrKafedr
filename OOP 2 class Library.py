from pydantic import BaseModel, conint


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    """
    Класс описывает книги
    """
    id_: int = conint(gt=0)
    name: str
    pages: int = conint(gt=0)


class Library:
    """
    Класс описывает библиотеку
    """
    id_to_added_book = 1 # Идентификатор для первой книги добавляемой в библиотеку

    def __init__(self, books = None):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: список книг в библиотеке
        """
        if books is None:
            self.books = [] # Если книг нет, возращаем пустой список
        else:
            self.books = books # Возвращаем список книг

    def get_next_book_id(self):
        """
        Функция позволяющая получить идентификатор для добавления новой книги в библиотеку

        :return: Новый идентификатор
        """
        if not self.books:
            return self.id_to_added_book  # Если книг нет, возвращаем 1
        else:
            self.id_to_added_book += self.books[-1].id_  # Идентификатор последней книги
            return self.id_to_added_book  # Возвращаем идентификатор увеличенный на 1

    def get_index_by_book_id(self, id: int):
        """
        Функция позволяющая найти индекс книги в списке

        :param id: идентификатор искомой книги
        :return: индекс искомой книги
        """
        for index, book in enumerate(self.books):
            if id == book.id_:
                return index  # Если книга с заданным идентификатором существует возвращаем её индекс в списке

        raise ValueError("Книги с запрашиваемым id не существует") # Если книга не найдена возвращаем ValueError

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
