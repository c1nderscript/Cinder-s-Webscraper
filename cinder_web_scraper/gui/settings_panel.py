"""Application settings panel."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Any, Dict

from cinder_web_scraper.utils import config_manager


class SettingsPanel:
    """Simple settings panel."""

    def __init__(self, parent: tk.Widget | None = None) -> None:
        self.parent = parent
        self.window: tk.Toplevel | None = None
        self.settings: Dict[str, Any] = {}
        self.logging_var: tk.BooleanVar | None = None

    def open(self) -> None:
        """Open the settings panel window."""

        if not self.parent:
            raise RuntimeError("Parent widget is not set")

        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.deiconify()
            return

        self.settings = config_manager.load_config("data/config.json").get(
            "settings", {}
        )
        self.window = tk.Toplevel(self.parent)
        self.window.title("Settings")
        self._setup_ui()

    def _setup_ui(self) -> None:
        assert self.window is not None

        frame = ttk.Frame(self.window, padding=10)
        frame.grid(sticky="nsew")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.logging_var = tk.BooleanVar(value=self.settings.get("logging", False))
        ttk.Checkbutton(
            frame, text="Enable logging", variable=self.logging_var
        ).grid(row=0, column=0, sticky="w")

        ttk.Button(frame, text="Save", command=self._save).grid(
            row=1, column=0, sticky="e", pady=5
        )

    def _save(self) -> None:
        """Save settings and close the panel.

        The current logging option is persisted to ``data/config.json`` using
        ``config_manager``. A message box notifies the user whether the save was
        successful and the settings window is closed afterwards.
        """

        assert self.logging_var is not None
        self.settings["logging"] = self.logging_var.get()
        config = config_manager.load_config("data/config.json")
        config["settings"] = self.settings
        if config_manager.save_config(config, "data/config.json"):
            messagebox.showinfo("Settings", "Settings saved")
        else:
            messagebox.showerror("Settings", "Failed to save settings")
        if self.window is not None:
            self.window.destroy()

