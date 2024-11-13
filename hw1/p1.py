def middle_printer(inp: str) -> str:
    """
    Return the middle character of the input string, or the two middle characters if the string length is even.

    :param inp: The string to find the middle character in.
    :return: The middle character of the string, or the two middle characters if the string length is even.
    """
    assert inp
    assert isinstance(inp, str)

    return inp[len(inp) // 2] if len(inp) % 2 else inp[len(inp) // 2 - 1 : len(inp) // 2 + 1]


def main():
    assert middle_printer('test'), 'es'
    assert middle_printer('testing'), 't'
    assert middle_printer('tes'), 'e'
    assert middle_printer('te'), 'te'
    assert middle_printer('t'), 't'
    try:
        middle_printer('')
    except AssertionError:
        pass
    else:
        raise AssertionError
    try:
        middle_printer(123)
    except AssertionError:
        pass
    else:
        raise AssertionError


if __name__ == '__main__':
    main()
