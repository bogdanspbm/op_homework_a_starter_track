"""
Алгоритмы работы с простыми числами.
Цель: реализовать функции для проверки простоты и поиска наибольшего простого числа.
"""


def is_prime(n: int) -> bool:
    """
    Проверка, является ли число простым (наивная реализация).

    🔹 Примеры:
    is_prime(2) -> True
    is_prime(15) -> False
    is_prime(17) -> True
    """
    raise NotImplementedError("implement me")


def is_prime_fast(n: int) -> bool:
    """
    Проверка, является ли число простым (оптимизированная версия).
    Авто-тесты пройдут, только в случае реального улучшения производительности.

    🔹 Примеры:
    is_prime_fast(2) -> True
    is_prime_fast(49) -> False
    is_prime_fast(97) -> True
    """
    raise NotImplementedError("implement me")


def find_largest_prime(limit: int, use_fast: bool = False) -> int:
    """
    Поиск наибольшего простого числа в диапазоне от 2 до limit.
    Если use_fast=True — используется оптимизированная проверка (is_prime_fast).

    Возвращает:
      - наибольшее простое число ≤ limit
      - -1, если простое число не найдено

    🔹 Примеры:
    find_largest_prime(10) -> 7
    find_largest_prime(20) -> 19
    find_largest_prime(2) -> 2
    find_largest_prime(1) -> -1
    """
    raise NotImplementedError("implement me")
