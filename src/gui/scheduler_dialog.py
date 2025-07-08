"""Dialog for scheduling scraping tasks."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional

from src.scheduling.schedule_manager import ScheduleManager


class SchedulerDialog:
    """UI dialog for configuring scraping schedules."""

    def __init__(self, parent: Optional[tk.Widget], manager: ScheduleManager) -> None:
        """Initialize the dialog.

        Args:
            parent: Parent widget for this dialog.
            manager: ``ScheduleManager`` instance that stores scheduled jobs.
        """

        self.parent = parent
        self.manager = manager
        self.window: Optional[tk.Toplevel] = None
        self.name_var: Optional[tk.StringVar] = None
        self.interval_var: Optional[tk.IntVar] = None

    # ------------------------------------------------------------------ UI ---
    def open(self) -> None:
        """Open the scheduler dialog window."""

        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.deiconify()
            return

        self.window = tk.Toplevel(self.parent)
        self.window.title("Schedule Task")
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Create widgets for scheduling a new task."""

        frame = ttk.Frame(self.window, padding=10)
        frame.grid(sticky="nsew")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.name_var = tk.StringVar()
        self.interval_var = tk.IntVar(value=60)

        ttk.Label(frame, text="Task Name:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.name_var).grid(
            row=0, column=1, sticky="ew"
        )

        ttk.Label(frame, text="Interval (s):").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.interval_var).grid(
            row=1, column=1, sticky="ew"
        )

        add_btn = ttk.Button(frame, text="Add", command=self._on_add)
        add_btn.grid(row=2, column=0, columnspan=2, pady=5)

        frame.columnconfigure(1, weight=1)

    # -------------------------------------------------------------- Logic ---
    def _on_add(self) -> None:
        name = self.name_var.get().strip() if self.name_var else ""
        try:
            interval = int(self.interval_var.get() if self.interval_var else 0)
        except ValueError:
            interval = 0

        if not name or interval <= 0:
            messagebox.showerror(
                "Invalid", "Provide a task name and a positive interval"
            )
            return

        self.manager.add_task(name, lambda: None, interval)
        messagebox.showinfo(
            "Scheduled", f"Task '{name}' scheduled every {interval} seconds."
        )
        if self.window:
            self.window.destroy()
