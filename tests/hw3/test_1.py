# Тесты для задания 1 ДЗ 3


from dataclasses import dataclass

import pytest

from hw3.p1 import sum_distance


@dataclass
class ValidationCase:
    frm: int
    to: int
    expected_result: int


hw3_p1_cases: tuple[ValidationCase, ...] = (
    ValidationCase(frm=1, to=5, expected_result=15),
    ValidationCase(frm=5, to=1, expected_result=15),
    ValidationCase(frm=5, to=5, expected_result=5),
    ValidationCase(frm=1, to=1, expected_result=1),
    ValidationCase(frm=1, to=0, expected_result=1),
)


@pytest.mark.parametrize('validation_case', hw3_p1_cases)
def test_hw3_p1(validation_case: ValidationCase):
    assert sum_distance(validation_case.frm, validation_case.to) == validation_case.expected_result
