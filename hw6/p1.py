"""Реализовать класс Account, который отражает абстракцию базового
поведения банковского аккаунта:

● создать банковский аккаунт с параметрами: имя; стартовый баланс с
которым зарегистрирован аккаунт; история операций*;

● реализовать два метода, которые позволяют положить деньги на счёт
или снять деньги со счёта;

● продумать, как можно хранить историю поступления или снятия
денег, чтобы с ней было удобно работать*.
"""

from collections import UserList
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class Transaction:
    """Отображает транзакцию банковского аккаунта.

    Не допускает редактирования после создания (frozen), поэтому же нет __post_init__.

    Args:
        amount: Сумма транзакции.
        sid: Уникальный идентификатор транзакции, например, uuid4()[:8].
        created_at: Время создания транзакции (UTC).
    """
    sid: str
    created_at: datetime
    amount: Decimal

    def __repr__(self) -> str:
        return f'{self.sid}\t{self.created_at}\t{self.amount}'

    def __eq__(self, other: 'Transaction') -> bool:
        return self.sid == other.sid

    def __lt__(self, other: 'Transaction') -> bool:
        return self.created_at < other.created_at

    def __le__(self, other: 'Transaction') -> bool:
        return self.created_at <= other.created_at

    def __gt__(self, other: 'Transaction') -> bool:
        return self.created_at > other.created_at

    def __ge__(self, other: 'Transaction') -> bool:
        return self.created_at >= other.created_at


class TransactionHistory(UserList):
    """История транзакций банковского аккаунта.

    Основная идея, что если потребуется расширить операции над множествами - их `удобно` будет расширить тут + UserList хоть и медленнее, зато, безопасен для расширения.
    """
    pass


@dataclass(slots=True)
class Account:
    name: str
    balance: Decimal
    sid: str = None
    history: TransactionHistory = None

    def __post_init__(self):
        if self.sid is None:
            self.sid = f"{uuid4()}"[:8]
        if self.history is None:
            self.history = TransactionHistory()

    def __str__(self) -> str:
        return f'{self.name} - {self.balance}'

    def __repr__(self):
        return f'{self.name}\t{self.balance}\t{self.history}'

    def __eq__(self, other: 'Account') -> bool:
        return self.sid == other.sid

    def _balance_operation(self, amount: Decimal, increase: bool) -> None:
        """Операция над балансом.

        Args:
            amount: Сумма операции.
            increase: True - положить деньги, False - снять деньги.
        """

        if increase:
            self.balance += amount
        else:
            self.balance -= amount
        self.history.append(Transaction(amount=amount, created_at=datetime.now(tz=timezone.utc), sid=f"{uuid4()}"[:8]))

    def deposit(self, amount: Decimal) -> None:
        """Увеличить баланс."""
        self._balance_operation(amount=amount, increase=True)

    def withdraw(self, amount: Decimal) -> None:
        """Уменьшить баланс."""
        self._balance_operation(amount=amount, increase=False)

    @property
    def last_transaction(self) -> Transaction | None:
        return self.history[-1] if self.history else None

    @property
    def first_transaction(self) -> Transaction | None:
        return self.history[0] if self.history else None


def main() -> None:
    pass


if __name__ == '__main__':
    main()
