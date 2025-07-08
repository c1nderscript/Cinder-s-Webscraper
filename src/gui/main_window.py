"""GUI main window for the scraper application."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional

from src.gui.scheduler_dialog import SchedulerDialog
from src.gui.settings_panel import SettingsPanel
from src.gui.website_manager import WebsiteManager
from src.scheduling.schedule_manager import ScheduleManager


class MainWindow:
    """Main application window for launching dialogs and managing state."""

    def __init__(self, root: Optional[tk.Tk] = None) -> None:
        """Initialize the main window instance.

        Args:
            root: Optional ``tk.Tk`` instance. If ``None`` a new root window is
                created.
        """
        self.root = root or tk.Tk()
        self.root.title("Cinder Web Scraper")

        # Core managers and dialogs
        self.schedule_manager = ScheduleManager()
        self.website_manager = WebsiteManager(self.root)
        self.scheduler_dialog = SchedulerDialog(self.root, self.schedule_manager)
        self.settings_panel = SettingsPanel(self.root, {})

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Create widgets for the main window."""

        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        btn_websites = ttk.Button(
            frame, text="Manage Websites", command=self.website_manager.open
        )
        btn_schedule = ttk.Button(
            frame, text="Scheduler", command=self.scheduler_dialog.open
        )
        btn_settings = ttk.Button(
            frame, text="Settings", command=self.settings_panel.open
        )
        btn_quit = ttk.Button(frame, text="Quit", command=self.root.destroy)

        for btn in (btn_websites, btn_schedule, btn_settings, btn_quit):
            btn.pack(fill="x", pady=5)

    def show_error(self, message: str) -> None:
        """Display a user-friendly error message."""

        messagebox.showerror("Error", message)

    def show(self) -> None:
        """Display the main window and start the Tkinter main loop."""

        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.root.destroy()
