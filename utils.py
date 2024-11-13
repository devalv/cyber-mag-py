import time
from typing import Any, Callable


def timer(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result: Any = func(*args, **kwargs)
        execution_time: float = time.time() - start_time
        print(f'\nВремя выполнения: {int(execution_time)} сек.\n')  # noqa T20
        return result, execution_time

    return wrapper
