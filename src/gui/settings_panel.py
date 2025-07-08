"""Application settings panel."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Any, Dict, Optional


class SettingsPanel:
    """Simple dialog for editing application settings."""

    def __init__(self, parent: Optional[tk.Widget], config: Dict[str, Any]) -> None:
        """Initialize the panel.

        Args:
            parent: Parent widget for the panel.
            config: Dictionary containing application settings.
        """

        self.parent = parent
        self.config = config
        self.window: Optional[tk.Toplevel] = None
        self.debug_var: Optional[tk.BooleanVar] = None

    # ------------------------------------------------------------------ UI ---
    def open(self) -> None:
        """Open the settings panel window."""

        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.deiconify()
            return

        self.window = tk.Toplevel(self.parent)
        self.window.title("Settings")
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Create widgets for settings options."""

        frame = ttk.Frame(self.window, padding=10)
        frame.grid(sticky="nsew")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.debug_var = tk.BooleanVar(value=self.config.get("debug", False))
        debug_cb = ttk.Checkbutton(
            frame, text="Enable Debug Logging", variable=self.debug_var
        )
        debug_cb.grid(row=0, column=0, sticky="w")

        save_btn = ttk.Button(frame, text="Save", command=self._save)
        save_btn.grid(row=1, column=0, pady=5, sticky="e")

    # -------------------------------------------------------------- Logic ---
    def _save(self) -> None:
        self.config["debug"] = bool(self.debug_var.get() if self.debug_var else False)
        messagebox.showinfo("Settings Saved", "Settings have been updated.")
        if self.window:
            self.window.destroy()
