"""Application settings panel."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class SettingsPanel:
    """Simple settings window."""

    def __init__(self, parent: tk.Widget | None = None) -> None:
        self.parent = parent or tk.Tk()
        self.window = tk.Toplevel(self.parent)
        self.window.title("Settings")
        self.frame = ttk.Frame(self.window, padding=10)
        self.frame.grid(sticky="nsew")
        ttk.Label(self.frame, text="Settings").grid(row=0, column=0)

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def open(self) -> None:
        """Open the settings panel window."""

        self.window.deiconify()
        self.window.wait_window()
