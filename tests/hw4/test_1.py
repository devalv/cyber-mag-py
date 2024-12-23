# Тесты для задания 1 ДЗ 4

from dataclasses import dataclass
from typing import Any

import pytest

from hw4.p1 import PurchasesLine, purchase_log_parser, purchase_log_reader


@dataclass(frozen=True, slots=True)
class LogParserValidationCase:
    input: dict[str, Any]
    expected_result: PurchasesLine


log_parser_cases: tuple[LogParserValidationCase, ...] = (
    LogParserValidationCase(
        input={'category': 'Продукты', 'user_id': '1840e0b9d4'},
        expected_result=PurchasesLine(user_id='1840e0b9d4', category='Продукты'),
    ),
    LogParserValidationCase(
        input={'category': 'Электроника', 'user_id': '4e4f90fcfb'},
        expected_result=PurchasesLine(user_id='4e4f90fcfb', category='Электроника'),
    ),
    LogParserValidationCase(
        input={'user_id': 'afea8d72fc', 'category': 'Электроника'},
        expected_result=PurchasesLine(user_id='afea8d72fc', category='Электроника'),
    ),
)


@pytest.mark.parametrize('validation_case', log_parser_cases)
def test_purchase_log_parser(validation_case: LogParserValidationCase):
    assert next(purchase_log_parser(validation_case.input)) == validation_case.expected_result


@pytest.fixture
def fake_purchase_log_content() -> list[str]:
    return [
        '{"category": "category", "user_id": "user_id"}\n',
        '{"category": "Продукты", "user_id": "1840e0b9d4"}\n',
        '{"user_id": "afea8d72fc", "category": "Электроника"}\n',
    ]


@pytest.fixture
def fake_purchase_log_file(fs, fake_purchase_log_content):
    with open('./pytest_purchase_log.txt', encoding='utf-8', mode='w') as f:
        f.writelines(fake_purchase_log_content)
    yield f.file_path  # type: ignore[attr-defined]


def test_purchase_log_reader(fake_purchase_log_file):
    assert list(purchase_log_reader(fake_purchase_log_file)) == [
        PurchasesLine(user_id='1840e0b9d4', category='Продукты'),
        PurchasesLine(user_id='afea8d72fc', category='Электроника'),
    ]
