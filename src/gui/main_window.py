"""GUI main window for the scraper application."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class MainWindow:
    """Main application window."""

    def __init__(self) -> None:
        """Initialize the main window instance."""

        self.root = tk.Tk()
        self.root.title("Cinder Web Scraper")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid(sticky="nsew")
        ttk.Label(self.frame, text="Cinder Web Scraper").grid(row=0, column=0)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def show(self) -> None:
        """Display the main window."""

        self.root.mainloop()
