def middle_printer(inp: str) -> str:
    """
    Return the middle character of the input string, or the two middle characters if the string length is even.

    :param inp: The string to find the middle character in.
    :return: The middle character of the string, or the two middle characters if the string length is even.
    """
    assert inp, 'Внимание, строка пуста!'
    assert isinstance(inp, str), 'Внимание, введено не строковое значение!'

    return inp[len(inp) // 2] if len(inp) % 2 else inp[len(inp) // 2 - 1 : len(inp) // 2 + 1]


def main():
    print(middle_printer(input('Введите слово:')))  # noqa T201


if __name__ == '__main__':
    main()
