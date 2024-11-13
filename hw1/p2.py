from enum import IntEnum
from typing import Generator


class Variant(IntEnum):
    """Варианты поиска идеальных пар."""

    INPLACE = 1
    GENERATOR = 2


def naive_inplace_matcher(boys: list[str], girls: list[str]) -> list[str]:
    """Поиск идеальных пар (наивная реализация с сортировкой исходного списка)."""
    boys.sort()
    girls.sort()
    return [f'{boys[i]} и {girls[i]}' for i in range(len(girls))]


def gen_matcher(boys: list[str], girls: list[str]) -> Generator[str, None, None]:
    """Поиск идеальных пар (альтернативный вариант на генераторах с копией исходного списка)."""
    _boys, _girls = boys.copy(), girls.copy()
    _boys.sort()
    _girls.sort()
    for i in range(len(_girls)):
        yield f'{_boys[i]} и {_girls[i]}'


def stdo_results(boys: list[str], girls: list[str], variant: Variant = Variant.INPLACE) -> None:
    """Вывод результата на экран."""

    try:
        # validation
        assert boys, 'Внимание, список мальчиков пуст!'
        assert girls, 'Внимание, список девочек пуст!'
        assert len(boys) == len(girls), 'Внимание, кто-то может остаться без пары!'

        match variant:
            case Variant.INPLACE:
                result: list[str] = naive_inplace_matcher(boys, girls)
            case Variant.GENERATOR:
                result: Generator[str, None, None] = gen_matcher(boys, girls)  # type: ignore[no-redef]
            case _:
                raise NotImplementedError(f'Вариант {variant} не реализован!')
    except (AssertionError, NotImplementedError) as err:
        print(f'Результат:\n{err}')  # noqa T20
    else:
        print('Результат:\nИдеальные пары:')  # noqa T20
        for pair in result:
            print(pair)  # noqa T20


def main():
    b1, g1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard'], ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    # stdo_results(b1, g1, Variant.GENERATOR)  # noqa ERA
    stdo_results(b1, g1, Variant.INPLACE)


if __name__ == '__main__':
    main()
