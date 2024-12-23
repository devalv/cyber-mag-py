"""
Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
● строку;
● offset — число символов, на которое нужно обрезать строку слева;
● repetitions — сколько раз нужно повторить строку перед возвратом
получившейся строки.
Число символов для среза по умолчанию равно 0, а количество повторений —
1.
Функция должна возвращать полученную строку.
"""


def trim_and_repeat(text: str, offset: int = 0, repetitions: int = 1) -> str:
    return text[offset:] * repetitions


def main():
    tx = input('Введите текст: ').strip()
    offset, repetitions = map(int, input('Введите offset и  repetitions через пробел: ').split())
    result: int = trim_and_repeat(text=tx, offset=offset, repetitions=repetitions)  # type: ignore[assignment]
    print(f'Результат: {result}')  # noqa T201


if __name__ == '__main__':
    main()
