"""Provides a basic scheduler for executing queued callables."""

from typing import Any, Callable, Dict, List, Tuple


class TaskScheduler:
    """Simple in-memory task scheduler."""

    def __init__(self) -> None:
        """Initialize the scheduler."""
        self.tasks: List[Tuple[Callable[..., Any], Tuple[Any, ...], Dict[str, Any]]] = (
            []
        )

    def add_task(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
        """Add a task callable with arguments.

        Args:
            func: The callable to execute.
            *args: Positional arguments for ``func``.
            **kwargs: Keyword arguments for ``func``.
        """
        self.tasks.append((func, args, kwargs))

    def run_all(self) -> None:
        """Run all scheduled tasks in the order they were added."""
        for func, args, kwargs in list(self.tasks):
            func(*args, **kwargs)
        self.tasks.clear()
