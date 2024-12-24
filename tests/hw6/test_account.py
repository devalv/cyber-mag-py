from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

import pytest

from hw6.p1 import Account, Transaction, TransactionHistory


def test_account_defaults():
    account: Account = Account(name='pytest', balance=Decimal(100.0))
    assert account.sid
    assert isinstance(account.history, TransactionHistory) and not account.history


@dataclass(frozen=True, slots=True)
class AccountBalanceCase:
    increment: bool
    account: Account
    operation_amount: Decimal
    expected_balance: Decimal


account_balance_cases: tuple[AccountBalanceCase, ...] = (
    AccountBalanceCase(
        account=Account(name='pytest', balance=Decimal(100.0)),
        operation_amount=Decimal(10.0),
        expected_balance=Decimal(110.0),
        increment=True,
    ),
    AccountBalanceCase(
        account=Account(name='pytest', balance=Decimal(100.0)),
        operation_amount=Decimal(5.5),
        expected_balance=Decimal(94.5),
        increment=False,
    ),
)


@pytest.mark.parametrize('validation_case', account_balance_cases)
def test_account_balance(validation_case: AccountBalanceCase):
    initial_trans_len: int = len(validation_case.account.history) if validation_case.account.history else 0
    if validation_case.increment:
        validation_case.account.deposit(validation_case.operation_amount)
    else:
        validation_case.account.withdraw(validation_case.operation_amount)
    assert validation_case.account.balance == validation_case.expected_balance
    assert len(validation_case.account.history) if validation_case.account.history else 0 == initial_trans_len + 1


@dataclass(frozen=True, slots=True)
class AccountStrReprCase:
    account: Account
    expected_str: str
    expected_repr: str


account_str_repr_cases: tuple[AccountStrReprCase, ...] = (
    AccountStrReprCase(
        account=Account(name='pytest', balance=Decimal(100.0), sid='2b92d689', history=TransactionHistory()),
        expected_str='pytest - 100',
        expected_repr='2b92d689\tpytest\t100\t[]',
    ),
    AccountStrReprCase(
        account=Account(
            name='pytes',
            balance=Decimal('1.12'),
            sid='2b92d689',
            history=TransactionHistory([
                Transaction(
                    amount=Decimal('1.0'),
                    created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'),
                    sid='1',
                    increase=True,
                ),
                Transaction(
                    amount=Decimal('3.21'),
                    created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'),
                    sid='2',
                    increase=False,
                ),
            ]),
        ),
        expected_str='pytes - 1.12',
        expected_repr='2b92d689\tpytes\t1.12\t[1	2024-01-01 00:00:00	+	1.0, 2	2024-01-01 00:00:00	-	3.21]',
    ),
)


@pytest.mark.parametrize('validation_case', account_str_repr_cases)
def test_account_str_repr(validation_case: AccountStrReprCase):
    assert f'{validation_case.account!s}' == validation_case.expected_str
    assert f'{validation_case.account!r}' == validation_case.expected_repr


def test_account_eq():
    account_1: Account = Account(name='pytest', balance=Decimal(100.0), sid='1')
    account_2: Account = Account(name='unitttest', balance=Decimal(100.0), sid='2')
    account_3: Account = Account(name='pytesty', balance=Decimal(100.0), sid='1')
    assert account_1 != account_2
    assert account_1 == account_3


@dataclass(frozen=True, slots=True)
class AccountRollbackCase:
    account: Account
    rollback_sid: str
    expected_balance: Decimal


account_rollback_cases: tuple[AccountRollbackCase, ...] = (
    AccountRollbackCase(
        account=Account(
            name='pytest',
            balance=Decimal(100.0),
            sid='1',
            history=TransactionHistory([
                Transaction(
                    amount=Decimal('1.0'),
                    created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'),
                    sid='1',
                    increase=True,
                ),
                Transaction(
                    amount=Decimal('3.21'),
                    created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'),
                    sid='2',
                    increase=False,
                ),
            ]),
        ),
        rollback_sid='1',
        expected_balance=Decimal('99.0'),
    ),
    AccountRollbackCase(
        account=Account(
            name='pytest',
            balance=Decimal(100.0),
            sid='1',
            history=TransactionHistory([
                Transaction(
                    amount=Decimal('1.0'),
                    created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'),
                    sid='1',
                    increase=True,
                ),
                Transaction(
                    amount=Decimal('3.21'),
                    created_at=datetime.strptime('2024-01-01', '%Y-%m-%d'),
                    sid='2',
                    increase=False,
                ),
            ]),
        ),
        rollback_sid='2',
        expected_balance=Decimal('103.21'),
    ),
)


@pytest.mark.parametrize('validation_case', account_rollback_cases)
def test_rollback(validation_case: AccountRollbackCase):
    validation_case.account.rollback(validation_case.rollback_sid)
    assert validation_case.account.balance == validation_case.expected_balance
