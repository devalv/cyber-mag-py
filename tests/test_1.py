from dataclasses import dataclass

import pytest

from hw1.p1 import middle_printer


@dataclass(frozen=True, slots=True)
class ValidationCase:
    word: str
    expected_result: str
    is_err: bool = False


hw1_p1_cases: tuple[ValidationCase, ...] = (
    ValidationCase('test', 'es'),
    ValidationCase('testing', 't'),
    ValidationCase('tes', 'e'),
    ValidationCase('te', 'te'),
    ValidationCase('t', 't'),
    ValidationCase('', 'Внимание, строка пуста!', True),
    ValidationCase(123, 'Внимание, введено не строковое значение!', True),  # type: ignore
)


@pytest.mark.parametrize('validation_case', hw1_p1_cases)
def test_hw1_p2(validation_case: ValidationCase):
    try:
        result: str = middle_printer(validation_case.word)
    except AssertionError as err:
        if not validation_case.is_err:
            raise
        assert err.args[0] == validation_case.expected_result
    else:
        if validation_case.is_err:
            raise AssertionError(f'Ожидаемая ошибка: {validation_case.expected_result}')
