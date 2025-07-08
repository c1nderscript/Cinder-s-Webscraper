"""Manage websites to be scraped."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import List


class WebsiteManager:
    """Manage website configuration logic."""

    def __init__(self, parent: tk.Widget | None = None) -> None:
        """Initialize the manager without creating a window.

        Args:
            parent: Optional parent widget.
        """
        self.parent = parent
        self.websites: List[str] = []
        self.window: tk.Toplevel | None = None
        self.listbox: tk.Listbox | None = None
        self.url_var = tk.StringVar() if parent else None

    def open(self) -> None:
        """Open the website management window."""

        if not self.parent:
            raise RuntimeError("Parent widget is not set")

        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.deiconify()
            return

        self.window = tk.Toplevel(self.parent)
        self.window.title("Manage Websites")
        self._setup_ui()

    def _setup_ui(self) -> None:
        assert self.window is not None

        frame = ttk.Frame(self.window, padding=10)
        frame.grid(sticky="nsew")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.url_var = tk.StringVar()
        ttk.Label(frame, text="Website URL:").grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(frame, textvariable=self.url_var, width=40)
        entry.grid(row=0, column=1, sticky="ew", padx=5)
        ttk.Button(frame, text="Add", command=self._add_from_entry).grid(
            row=0, column=2, padx=5
        )

        self.listbox = tk.Listbox(frame, height=10)
        self.listbox.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=5)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.grid(row=1, column=2, sticky="ns", pady=5)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        ttk.Button(frame, text="Remove", command=self._remove_selected).grid(
            row=2, column=0, sticky="w", pady=5
        )

        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)

    def _add_from_entry(self) -> None:
        url = self.url_var.get().strip() if self.url_var else ""
        if not url:
            messagebox.showerror("Error", "URL cannot be empty")
            return
        self.add_website(url)
        if self.url_var:
            self.url_var.set("")

    def add_website(self, url: str) -> None:
        """Add a website to the list of sites to scrape."""

        if url not in self.websites:
            self.websites.append(url)
            if self.listbox is not None:
                self.listbox.insert(tk.END, url)

    def remove_website(self, url: str) -> None:
        """Remove a website from the scrape list."""

        if url in self.websites:
            index = self.websites.index(url)
            self.websites.remove(url)
            if self.listbox is not None:
                self.listbox.delete(index)

    def _remove_selected(self) -> None:
        if self.listbox is None:
            return
        sel = self.listbox.curselection()
        if not sel:
            return
        url = self.listbox.get(sel[0])
        self.remove_website(url)

