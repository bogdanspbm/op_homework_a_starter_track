"""
Работа с отсортированными массивами и базовыми алгоритмами:
- собственная сортировка
- классические сортировки
- структура данных SortedArray
- бинарный поиск
"""
from typing import Optional


# --------------------------
# 1. Реализация собственной сортировки
# --------------------------

def my_sort(arr: list[int]) -> list[int]:
    """
    Собственная сортировка «из головы».
    Реализуйте так, как представляете алгоритм самостоятельно.

    🔹 Примеры:
    my_sort([3, 1, 2]) -> [1, 2, 3]
    my_sort([5, 4, 3, 2, 1]) -> [1, 2, 3, 4, 5]
    """
    raise NotImplementedError("implement me")


# --------------------------
# 3. Классические сортировки
# --------------------------

def bubble_sort(arr: list[int]) -> list[int]:
    """
    Сортировка пузырьком.
    Проходимся по всем элементам, сравниваем его с соседом справа.
    Если элемент больше соседа справа — меняем их местами.
    Повторяем так, пока весь массив не будет отсортирован.

    🔹 Пример первой итерации:
    [3, 2, 1] → сравниваем 3 и 2 → меняем → [2, 3, 1]
                сравниваем 3 и 1 → меняем → [2, 1, 3]
    """
    raise NotImplementedError("implement me")


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Сортировка вставками.
    Берём элемент и вставляем его в массиве перед первым встречным элементом,
    который больше него. Так формируем отсортированную часть массива.
    Повторяем, пока не пройдём все элементы.

    🔹 Пример первой итерации (Начинаем со второго числа, так как первое равно само себе):
    [3, 2, 1] → берём 2 → вставляем перед 3 → [2, 3, 1]
    """
    raise NotImplementedError("implement me")


def selection_sort(arr: list[int]) -> list[int]:
    """
    Сортировка выбором.
    Находим минимальный элемент и вставляем его в начало массива.
    Повторяем для оставшейся части массива, пока всё не будет отсортировано.

    🔹 Пример первой итерации:
    [3, 2, 1] → минимальный элемент 1 → ставим в начало → [1, 3, 2]
    """
    raise NotImplementedError("implement me")


def merge_sort(arr: list[int]) -> list[int]:
    """
    ДОП. ЗАДАНИЕ - БЕЗ АВТО-ТЕСТОВ

    Сортировка слиянием.
    Рекурсивно делим массив на две части, пока длина части не будет равна 1 или 2 элементам.
    При выходе из рекурсии получаем два отсортированных массива и объединяем их
    в новый отсортированный.

    🔹 Пример первой итерации:
    [3, 2, 1] → делим на [3] и [2, 1]
    → сортируем [2, 1] → получаем [1, 2]
    → объединяем [3] и [1, 2] → [1, 2, 3]
    """
    raise NotImplementedError("implement me")


# --------------------------
# 4. Класс SortedArray
# --------------------------

class SortedArray:
    """
    Структура данных «отсортированный массив».
    Хранит данные в отсортированном виде и поддерживает методы insert, delete, get, has.
    """

    def __init__(self, data: Optional[list[int]] = None):
        """
        Инициализация массива.

        🔹 Примеры:
        SortedArray([3, 1, 2]) -> SortedArray([1, 2, 3])
        SortedArray([]) -> SortedArray([])
        """
        raise NotImplementedError("implement me")

    def insert(self, value: int) -> None:
        """
        Вставка элемента с сохранением порядка.

        🔹 Примеры:
        arr = SortedArray([1, 3, 5])
        arr.insert(4) -> SortedArray([1, 3, 4, 5])
        arr.insert(0) -> SortedArray([0, 1, 3, 4, 5])
        """
        raise NotImplementedError("implement me")

    def delete(self, value: int) -> None:
        """
        Удаление элемента, если он есть.

        🔹 Примеры:
        arr = SortedArray([1, 2, 3])
        arr.delete(2) -> SortedArray([1, 3])
        arr.delete(10) -> SortedArray([1, 3])  # без изменений
        """
        raise NotImplementedError("implement me")

    def get(self, index: int) -> int:
        """
        Получение элемента по индексу.

        🔹 Примеры:
        arr = SortedArray([1, 2, 3])
        arr.get(0) -> 1
        arr.get(2) -> 3
        """
        raise NotImplementedError("implement me")

    def has(self, value: int) -> bool:
        """
        Проверка наличия элемента через binary_search.

        🔹 Примеры:
        arr = SortedArray([1, 3, 5])
        arr.has(3) -> True
        arr.has(4) -> False
        """
        raise NotImplementedError("implement me")


# --------------------------
# 5. Бинарный поиск
# --------------------------

def binary_search(sorted_arr: SortedArray, target: int) -> int:
    """
    Бинарный поиск по SortedArray.
    Возвращает индекс элемента или -1, если элемент отсутствует.

    🔹 Примеры:
    arr = SortedArray([1, 3, 5, 7])
    binary_search(arr, 5) -> 2
    binary_search(arr, 2) -> -1
    """
    raise NotImplementedError("implement me")
