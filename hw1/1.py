def middle_printer(inp: str) -> str:
    # validation
    assert inp
    assert isinstance(inp, str)

    len_is_even: int = len(inp) % 2
    return inp[len(inp) // 2] if len_is_even else inp[len(inp) // 2 - 1 : len(inp) // 2 + 1]


def main():
    assert middle_printer('test'), 'es'
    assert middle_printer('testing'), 't'
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
