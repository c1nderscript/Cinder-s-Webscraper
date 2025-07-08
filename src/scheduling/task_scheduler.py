class TaskScheduler:
    """Simple in-memory task scheduler."""

    def __init__(self):
        self.tasks = []

    def add_task(self, func, *args, **kwargs):
        """Add a task callable with arguments."""
        self.tasks.append((func, args, kwargs))

    def run_all(self):
        """Run all scheduled tasks in the order they were added."""
        for func, args, kwargs in list(self.tasks):
            func(*args, **kwargs)
        self.tasks.clear()
