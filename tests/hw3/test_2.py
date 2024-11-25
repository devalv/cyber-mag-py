# Тесты для задания 2 ДЗ 3
from dataclasses import dataclass

import pytest

from hw3.p2 import trim_and_repeat


@dataclass
class ValidationCase:
    text: str
    offset: int
    repetitions: int
    expected_result: str


hw3_p2_cases: tuple[ValidationCase, ...] = (
    ValidationCase(text='test', offset=0, repetitions=1, expected_result='test'),
    ValidationCase(text='test', offset=0, repetitions=2, expected_result='testtest'),
    ValidationCase(text='test', offset=1, repetitions=1, expected_result='est'),
    ValidationCase(text='test', offset=1, repetitions=2, expected_result='estest'),
    ValidationCase(text='test', offset=2, repetitions=1, expected_result='st'),
    ValidationCase(text='test', offset=2, repetitions=2, expected_result='stst'),
    ValidationCase(text='test', offset=3, repetitions=1, expected_result='t'),
    ValidationCase(text='test', offset=3, repetitions=2, expected_result='tt'),
    ValidationCase(text='test', offset=4, repetitions=1, expected_result=''),
    ValidationCase(text='test', offset=4, repetitions=2, expected_result=''),
    ValidationCase(text='', offset=0, repetitions=1, expected_result=''),
    ValidationCase(text='', offset=1, repetitions=2, expected_result=''),
)


@pytest.mark.parametrize('validation_case', hw3_p2_cases)
def test_hw3_p2(validation_case: ValidationCase):
    assert (
        trim_and_repeat(validation_case.text, validation_case.offset, validation_case.repetitions)
        == validation_case.expected_result
    )
