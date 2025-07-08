"""GUI main window for the scraper application."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from src.utils.logger import get_logger, log_exception

logger = get_logger(__name__)


class MainWindow:
    """Main application window."""

    def __init__(self) -> None:
        """Initialize the window."""

        self.root = tk.Tk()
        self.root.title("Cinder's Web Scraper")

    def show(self) -> None:
        """Display the main window with basic error handling."""

        try:
            self.root.mainloop()
        except Exception as exc:  # pragma: no cover - GUI errors in tests
            messagebox.showerror(
                "Application Error",
                "An unexpected error occurred. See log for details.",
            )
            log_exception(logger, "Unhandled exception in GUI", exc)


