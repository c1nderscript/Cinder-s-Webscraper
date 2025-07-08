"""Dialog for scheduling scraping tasks."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable, Optional


class SchedulerDialog:
    """UI dialog for configuring scraping schedules."""

    def __init__(
        self,
        parent: tk.Widget | None = None,
        callback: Optional[Callable[[int], None]] = None,
    ) -> None:
        """Initialize the dialog without creating the window."""

        self.parent = parent
        self.callback = callback
        self.window: tk.Toplevel | None = None
        self.interval_var = tk.StringVar() if parent else None

    def open(self) -> None:
        """Open the scheduler dialog window."""

        if not self.parent:
            raise RuntimeError("Parent widget is not set")

        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.deiconify()
            return

        self.window = tk.Toplevel(self.parent)
        self.window.title("Schedule Task")
        self._setup_ui()

    def _setup_ui(self) -> None:
        assert self.window is not None

        frame = ttk.Frame(self.window, padding=10)
        frame.grid(sticky="nsew")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        ttk.Label(frame, text="Frequency:").grid(row=0, column=0, sticky="w")
        options = {"Hourly": 3600, "Daily": 86400, "Weekly": 604800}
        self.interval_var = tk.StringVar(value="3600")
        self.freq_combo = ttk.Combobox(
            frame, values=list(options.keys()), state="readonly"
        )
        self.freq_combo.grid(row=0, column=1, sticky="ew", padx=5)

        def _combo_selected(_event: object) -> None:
            sel = self.freq_combo.get()
            self.interval_var.set(str(options.get(sel, 0)))

        self.freq_combo.bind("<<ComboboxSelected>>", _combo_selected)

        ttk.Label(frame, text="Custom seconds:").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.interval_var, width=10).grid(
            row=1, column=1, sticky="w", padx=5
        )

        ttk.Button(frame, text="Schedule", command=self._on_schedule).grid(
            row=2, column=0, columnspan=2, pady=5
        )

        frame.columnconfigure(1, weight=1)

    def _on_schedule(self) -> None:
        assert self.interval_var is not None
        try:
            seconds = int(float(self.interval_var.get()))
        except ValueError:
            messagebox.showerror("Error", "Invalid interval")
            return

        if self.callback:
            self.callback(seconds)
        if self.window is not None:
            self.window.destroy()

