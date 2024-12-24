from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

import pytest

from hw6.p1 import Transaction, TransactionHistory


@dataclass(frozen=True, slots=True)
class SidSearchCase:
    transactions: TransactionHistory | None = None
    sid_to_find: str | None = None
    expected_result: Transaction | None = None


sid_search_cases: tuple[SidSearchCase, ...] = (
    SidSearchCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='3', increase=True
            ),
        ]),
        sid_to_find='2',
        expected_result=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
        ),
    ),
    SidSearchCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='2', increase=True
            ),
        ]),
        sid_to_find='3',
        expected_result=None,
    ),
    SidSearchCase(transactions=TransactionHistory(), sid_to_find='3', expected_result=None),
)


@pytest.mark.parametrize('validation_case', sid_search_cases)
def test_search_by_sid(validation_case: SidSearchCase):
    assert validation_case.expected_result == validation_case.transactions.search_by_sid(validation_case.sid_to_find)  # type: ignore[union-attr]


@dataclass(frozen=True, slots=True)
class CreatedAtSearchCase:
    transactions: TransactionHistory | None = None
    date_to_find: datetime | None = None
    expected_result: Transaction | None = None


created_at_search_cases: tuple[CreatedAtSearchCase, ...] = (
    CreatedAtSearchCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
            ),
        ]),
        date_to_find=datetime.strptime('2024-01-03', '%Y-%m-%d'),
        expected_result=Transaction(
            amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
        ),
    ),
    CreatedAtSearchCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
        ]),
        date_to_find=datetime.strptime('2024-01-03', '%Y-%m-%d'),
        expected_result=None,
    ),
    CreatedAtSearchCase(
        transactions=TransactionHistory(),
        date_to_find=datetime.strptime('2024-01-03', '%Y-%m-%d'),
        expected_result=None,
    ),
)


@pytest.mark.parametrize('validation_case', created_at_search_cases)
def test_search_by_created_at(validation_case: CreatedAtSearchCase):
    assert (
        validation_case.transactions.search_by_created_at(  # type: ignore[union-attr]
            validation_case.date_to_find
        )
        == validation_case.expected_result
    )


@dataclass(frozen=True, slots=True)
class SortSearchCase:
    transactions: TransactionHistory | None = None
    expected_result: list[Transaction] | None = None


default_sort_cases: tuple[SortSearchCase, ...] = (
    SortSearchCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-04', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
            ),
        ]),
        expected_result=[
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-04', '%Y-%m-%d'), sid='1', increase=True
            ),
        ],
    ),
)


@pytest.mark.parametrize('validation_case', default_sort_cases)
def test_default_sort(validation_case: SortSearchCase):
    validation_case.transactions.sort()  # type: ignore[union-attr]
    assert validation_case.expected_result == validation_case.transactions


default_reverse_sort_cases: tuple[SortSearchCase, ...] = (
    SortSearchCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-04', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
            ),
        ]),
        expected_result=[
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-04', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=False
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
        ],
    ),
)


@pytest.mark.parametrize('validation_case', default_reverse_sort_cases)
def test_default_reverse_sort(validation_case: SortSearchCase):
    validation_case.transactions.sort(reverse=True)  # type: ignore[union-attr]
    assert validation_case.transactions == validation_case.expected_result


@dataclass(frozen=True, slots=True)
class RollbackCase:
    transactions: TransactionHistory | None = None
    sid_to_remove: str | None = None
    expected_result: list[Transaction] | None = None


rollback_cases: tuple[RollbackCase, ...] = (
    RollbackCase(
        transactions=TransactionHistory([
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-04', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-02', '%Y-%m-%d'), sid='2', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
            ),
        ]),
        sid_to_remove='2',
        expected_result=[
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-04', '%Y-%m-%d'), sid='1', increase=True
            ),
            Transaction(
                amount=Decimal('1.0'), created_at=datetime.strptime('2024-01-03', '%Y-%m-%d'), sid='3', increase=True
            ),
        ],
    ),
    RollbackCase(transactions=TransactionHistory(), sid_to_remove=None, expected_result=[]),
)


@pytest.mark.parametrize('validation_case', rollback_cases)
def test_rollback(validation_case: RollbackCase):
    validation_case.transactions.rollback_by_sid(validation_case.sid_to_remove)  # type: ignore[union-attr]
    assert validation_case.transactions == validation_case.expected_result
