"""
Реализуйте функцию sum_distance(from, to), которая суммирует все числа от
значения from до величины to включительно.
Примечание. Если пользователь задаст первое число, которое окажетсябольше второго, просто поменяйте их местами.
"""


# в задании указано, что 1й аргумент функции называется from - зарезервированное слово, сократил до frm
def sum_distance(frm: int, to: int) -> int:
    """
    Calculate the sum of all integers from `frm` to `to`, inclusive.

    If `frm` is greater than `to`, their values are swapped to ensure
    the summation is performed from the smaller to the larger number.

    :param frm: The starting integer of the range.
    :param to: The ending integer of the range.
    :return: The sum of all integers from `frm` to `to`.
    """
    if frm > to:
        frm, to = to, frm
    return sum(range(frm, to + 1))


def main():
    frm, to = map(int, input('Введите два числа через пробел: ').split())
    result: int = sum_distance(frm, to)
    print(f'Результат: {result}')  # noqa T201


if __name__ == '__main__':
    main()
