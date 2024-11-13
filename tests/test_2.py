from dataclasses import dataclass

import pytest

from hw1.p2 import Variant, stdo_results


@dataclass(frozen=True, slots=True)
class ValidationCase:
    boys: list
    girls: list
    matcher_variant: Variant
    expected_result: str


hw1_p2_cases: tuple[ValidationCase, ...] = (
    ValidationCase(list(), ['Masha'], Variant.INPLACE, 'Результат:\nВнимание, список мальчиков пуст!\n'),
    ValidationCase(list(), ['Masha'], Variant.GENERATOR, 'Результат:\nВнимание, список мальчиков пуст!\n'),
    ValidationCase(['Peter'], list(), Variant.INPLACE, 'Результат:\nВнимание, список девочек пуст!\n'),
    ValidationCase(['Peter'], list(), Variant.GENERATOR, 'Результат:\nВнимание, список девочек пуст!\n'),
    ValidationCase(list(), list(), Variant.INPLACE, 'Результат:\nВнимание, список мальчиков пуст!\n'),
    ValidationCase(list(), list(), Variant.GENERATOR, 'Результат:\nВнимание, список мальчиков пуст!\n'),
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        Variant.INPLACE,
        'Результат:\nВнимание, кто-то может остаться без пары!\n',
    ),
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        Variant.GENERATOR,
        'Результат:\nВнимание, кто-то может остаться без пары!\n',
    ),
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        Variant.INPLACE,
        'Результат:\nИдеальные пары:\nAlex и Emma\nArthur и Kate\nJohn и Kira\nPeter и Liza\nRichard и Trisha\n',
    ),
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        Variant.GENERATOR,
        'Результат:\nИдеальные пары:\nAlex и Emma\nArthur и Kate\nJohn и Kira\nPeter и Liza\nRichard и Trisha\n',
    ),
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        3,  # type: ignore
        'Результат:\nВариант 3 не реализован!\n',
    ),
)


@pytest.mark.parametrize('validation_case', hw1_p2_cases)
def test_hw1_p2(validation_case: ValidationCase, capsys):
    stdo_results(validation_case.boys, validation_case.girls, validation_case.matcher_variant)
    stdout: str = capsys.readouterr().out
    assert stdout == validation_case.expected_result
