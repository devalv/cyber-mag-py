import time
from enum import IntEnum
from typing import Any, Generator


class Variant(IntEnum):
    """Варианты поиска идеальных пар."""

    INPLACE = 1
    GENERATOR = 2


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result: Any = func(*args, **kwargs)
        execution_time: float = time.time() - start_time
        print(f'\nВремя выполнения: {int(execution_time)} сек.\n')  # noqa T20
        return result, execution_time

    return wrapper


def naive_inplace_matcher(boys: list[str], girls: list[str]) -> list[str]:
    """Поиск идеальных пар (наивная реализация с сортировкой исходного списка)."""
    assert boys, 'Внимание, список мальчиков пуст!'
    assert girls, 'Внимание, список девочек пуст!'
    assert len(boys) == len(girls), 'Внимание, кто-то может остаться без пары!'
    _boys, _girls = boys.copy(), girls.copy()
    boys.sort()
    girls.sort()
    return [f'{boys[i]} и {girls[i]}' for i in range(len(girls))]


def gen_matcher(boys: list[str], girls: list[str]) -> Generator[str, None, None]:
    """Поиск идеальных пар (альтернативный вариант на генераторах с копией исходного списка)."""
    assert boys, 'Внимание, список мальчиков пуст!'
    assert girls, 'Внимание, список девочек пуст!'
    assert len(boys) == len(girls), 'Внимание, кто-то может остаться без пары!'
    _boys, _girls = boys.copy(), girls.copy()
    _boys.sort()
    _girls.sort()
    for i in range(len(girls)):
        yield f'{boys[i]} и {girls[i]}'


@timer
def stdo_results(boys: list[str], girls: list[str], variant: Variant = Variant.INPLACE) -> None:
    """Вывод результата на экран."""
    try:
        match variant:
            case Variant.INPLACE:
                result: list[str] = naive_inplace_matcher(boys, girls)
            case Variant.GENERATOR:
                result: Generator[str, None, None] = gen_matcher(boys, girls)  # type: ignore[no-redef]
            case _:
                raise NotImplementedError(f'Вариант {variant} не реализован!')
    except AssertionError as err:
        print(f'Результат: {err}')  # noqa T20
    else:
        print('Результат:\nИдеальные пары:')  # noqa T20
        for pair in result:
            print(pair)  # noqa T20


# TODO: tests
def main():
    b1, g1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    # extra large lists
    # ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']), ['Внимание, кто-то может остаться без пары!']
    # empty list 1
    # empty list 2

    _, t1 = stdo_results(b1, g1, Variant.GENERATOR)
    _, t2 = stdo_results(b1, g1, Variant.INPLACE)
    print(f'Время работы генератора: {t1}\nВремя работы сортировки: {t2}')  # noqa T20


if __name__ == '__main__':
    main()
