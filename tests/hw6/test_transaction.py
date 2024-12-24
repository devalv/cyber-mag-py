from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any

import pytest

from hw6.p1 import Transaction


@dataclass(frozen=True, slots=True)
class TransactionCase:
    transaction1: Transaction
    transaction2: Any
    expected_result: bool


transaction_eq_cases: tuple[TransactionCase, ...] = (
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=1,
        expected_result=False,
    ),
)


@pytest.mark.parametrize('validation_case', transaction_eq_cases)
def test_eq(validation_case: TransactionCase):
    assert (validation_case.transaction1 == validation_case.transaction2) == validation_case.expected_result


transaction_lt_cases: tuple[TransactionCase, ...] = (
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=1,
        expected_result=False,
    ),
)


@pytest.mark.parametrize('validation_case', transaction_lt_cases)
def test_lt(validation_case: TransactionCase):
    try:
        assert (validation_case.transaction1 < validation_case.transaction2) == validation_case.expected_result
    except TypeError:
        if not isinstance(validation_case.transaction2, Transaction):
            assert not validation_case.expected_result


transaction_le_cases: tuple[TransactionCase, ...] = (
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=1,
        expected_result=False,
    ),
)


@pytest.mark.parametrize('validation_case', transaction_le_cases)
def test_le(validation_case: TransactionCase):
    try:
        assert (validation_case.transaction1 <= validation_case.transaction2) == validation_case.expected_result
    except TypeError:
        if not isinstance(validation_case.transaction2, Transaction):
            assert not validation_case.expected_result


transaction_gt_cases: tuple[TransactionCase, ...] = (
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=1,
        expected_result=False,
    ),
)


@pytest.mark.parametrize('validation_case', transaction_gt_cases)
def test_gt(validation_case: TransactionCase):
    try:
        assert (validation_case.transaction1 > validation_case.transaction2) == validation_case.expected_result
    except TypeError:
        if not isinstance(validation_case.transaction2, Transaction):
            assert not validation_case.expected_result


transaction_ge_cases: tuple[TransactionCase, ...] = (
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=False,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
        ),
        transaction2=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result=True,
    ),
    TransactionCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        transaction2=1,
        expected_result=False,
    ),
)


@pytest.mark.parametrize('validation_case', transaction_ge_cases)
def test_ge(validation_case: TransactionCase):
    try:
        assert (validation_case.transaction1 >= validation_case.transaction2) == validation_case.expected_result
    except TypeError:
        if not isinstance(validation_case.transaction2, Transaction):
            assert not validation_case.expected_result


@dataclass(frozen=True, slots=True)
class TransactionStrCase:
    transaction1: Transaction
    expected_result: str


transaction_str_cases: tuple[TransactionStrCase, ...] = (
    TransactionStrCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
        ),
        expected_result='1\t2024-01-01 00:00:00\t+\t1.0',
    ),
    TransactionStrCase(
        transaction1=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=False
        ),
        expected_result='1\t2024-01-01 00:00:00\t-\t1.0',
    ),
)


@pytest.mark.parametrize('validation_case', transaction_str_cases)
def test_str(validation_case: TransactionStrCase):
    assert str(validation_case.transaction1) == validation_case.expected_result
