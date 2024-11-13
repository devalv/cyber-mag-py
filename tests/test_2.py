from dataclasses import dataclass

import pytest

from hw1.p2 import gen_matcher, naive_inplace_matcher


@dataclass(frozen=True, slots=True)
class ValidationCase:
    boys: list
    girls: list
    expected_result: list | None = None
    expected_error: str | None = None


bad_cases: tuple[ValidationCase, ...] = (
    ValidationCase(list(), ['Masha'], None, 'Внимание, список мальчиков пуст!'),
    ValidationCase(['Peter'], list(), None, 'Внимание, список девочек пуст!'),
    ValidationCase(list(), list(), None, 'Внимание, список мальчиков пуст!'),
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        None,
        'Внимание, кто-то может остаться без пары!',
    ),
)


@pytest.mark.parametrize('validation_case', bad_cases)
def test_naive_bad_cases(validation_case: ValidationCase):
    try:
        r = naive_inplace_matcher(validation_case.boys, validation_case.girls)
    except AssertionError as err:
        assert err.args[0] == validation_case.expected_error
    else:
        raise AssertionError(''.join(r))


@pytest.mark.parametrize('validation_case', bad_cases)
def test_gen_bad_cases(validation_case: ValidationCase):
    try:
        r = gen_matcher(validation_case.boys, validation_case.girls)
    except AssertionError as err:
        assert err.args[0] == validation_case.expected_error
    else:
        raise AssertionError(''.join(r))


good_cases: tuple[ValidationCase, ...] = (
    ValidationCase(
        ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        ['Alex и Emma', 'Arthur и Kate', 'John и Kira', 'Peter и Liza', 'Richard и Trisha'],
        None,
    ),
)


@pytest.mark.parametrize('validation_case', good_cases)
def test_naive_good_cases(validation_case: ValidationCase):
    result = naive_inplace_matcher(validation_case.boys, validation_case.girls)
    assert result == validation_case.expected_result
