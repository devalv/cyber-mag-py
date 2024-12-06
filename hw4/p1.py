import json
from dataclasses import dataclass
from typing import Any, Generator


@dataclass(frozen=True, slots=True)
class PurchasesLine:
    user_id: str
    category: str


def purchase_log_parser(log_line: dict[str, Any]) -> Generator[PurchasesLine, None, None]:
    """
    Parse purchase log line and yield PurchasesLine.
    {"category": "Продукты", "user_id": "1840e0b9d4"} -> {"1840e0b9d4", "Продукты"}

    :param log_line: single purchase log line as a dictionary
    :yield: PurchasesLine
    :raises AssertionError: if log line is empty
    """
    assert log_line
    assert isinstance(log_line, dict)
    yield PurchasesLine(user_id=log_line['user_id'], category=log_line['category'])


def purchase_log_reader(file_path: str) -> Generator[PurchasesLine, None, None]:
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            parsed_line: dict[str, Any] = json.loads(line)
            # отсекаем записи с одинаковыми ключами, например, заголовки таблиц
            if set(parsed_line.keys()) == set(parsed_line.values()):
                continue
            # выполняем парсинг
            yield from purchase_log_parser(log_line=parsed_line)


def main() -> None:
    purchases: dict[str, str] = {line.user_id: line.category for line in purchase_log_reader('./purchase_log.txt')}
    assert list(purchases.items())[:2] == [('1840e0b9d4', 'Продукты'), ('4e4f90fcfb', 'Электроника')], (
        'Итоговые списки не совпадают!'
    )
    print('Всё прошло удачно!')  # noqa T201


if __name__ == '__main__':
    main()
