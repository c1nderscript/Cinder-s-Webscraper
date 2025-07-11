"""GUI main window for the scraper application."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable, Optional

from cinder_web_scraper.utils.logger import get_logger, log_exception
from cinder_web_scraper.utils.updater import update_application

logger = get_logger(__name__)


class MainWindow:
    """Main application window."""

    def __init__(
        self,
        root: tk.Tk | None = None,
        on_manage_sites: Optional[Callable[[], None]] = None,
        on_schedule: Optional[Callable[[], None]] = None,
        on_settings: Optional[Callable[[], None]] = None,
    ) -> None:
        """Initialize the main window instance."""
        self.root = root or tk.Tk()
        self.on_manage_sites = on_manage_sites
        self.on_schedule = on_schedule
        self.on_settings = on_settings

        self.status_var = tk.StringVar(value="Ready")
        self.site_listbox: tk.Listbox

        self._setup_ui()

    def _setup_ui(self) -> None:
        """Create all UI components."""
        self.root.title("Cinder's Web Scraper")

        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Update", command=self._update_app)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        self.root.config(menu=menubar)

        toolbar = ttk.Frame(self.root)
        ttk.Button(
            toolbar,
            text="Add Site",
            command=self._on_manage_sites,
        ).pack(side=tk.LEFT, padx=2, pady=2)
        ttk.Button(
            toolbar,
            text="Start Scraping",
            command=self._start_scraping,
        ).pack(side=tk.LEFT, padx=2, pady=2)
        ttk.Button(
            toolbar,
            text="Settings",
            command=self._on_settings,
        ).pack(side=tk.LEFT, padx=2, pady=2)
        ttk.Button(
            toolbar,
            text="Update",
            command=self._update_app,
        ).pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(fill=tk.X)

        list_frame = ttk.Frame(self.root)
        self.site_listbox = tk.Listbox(list_frame, height=10)
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.site_listbox.yview)
        self.site_listbox.configure(yscrollcommand=scrollbar.set)
        self.site_listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        actions = ttk.Frame(self.root)
        ttk.Button(actions, text="Start", command=self._start_scraping).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions, text="Stop", command=self._stop_scraping).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions, text="Schedule", command=self._on_schedule).pack(side=tk.LEFT, padx=5)
        ttk.Button(
            actions,
            text="Configure",
            command=self._on_manage_sites,
        ).pack(side=tk.LEFT, padx=5)
        actions.pack(pady=5)

        status = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status.pack(fill=tk.X, side=tk.BOTTOM)

    def _start_scraping(self) -> None:
        """Placeholder for starting scraping."""
        messagebox.showinfo("Scraper", "Scraping started")
        self.status_var.set("Scraping...")

    def _stop_scraping(self) -> None:
        """Placeholder for stopping scraping."""
        messagebox.showinfo("Scraper", "Scraping stopped")
        self.status_var.set("Stopped")

    def _on_manage_sites(self) -> None:
        if self.on_manage_sites:
            self.on_manage_sites()

    def _on_schedule(self) -> None:
        if self.on_schedule:
            self.on_schedule()

    def _on_settings(self) -> None:
        if self.on_settings:
            self.on_settings()

    def _update_app(self) -> None:
        """Run application update and show a message box with the result."""
        success, msg = update_application()
        if success:
            messagebox.showinfo("Update", f"Application updated:\n{msg}")
        else:
            messagebox.showerror("Update Failed", msg)

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
