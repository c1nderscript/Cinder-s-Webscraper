"""Manage websites to be scraped."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import List, Optional
from urllib.parse import urlparse


class WebsiteManager:
    """Manage website configuration logic and corresponding UI."""

    def __init__(self, parent: Optional[tk.Widget] = None) -> None:
        """Initialize the manager.

        Args:
            parent: Optional parent widget for ``Toplevel`` windows.
        """

        self.parent = parent
        self.websites: List[str] = []
        self.window: Optional[tk.Toplevel] = None
        self.listbox: Optional[tk.Listbox] = None
        self.entry: Optional[ttk.Entry] = None

    # ------------------------------------------------------------------ UI ---
    def open(self) -> None:
        """Open the website manager window."""

        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.deiconify()
            return

        self.window = tk.Toplevel(self.parent)
        self.window.title("Website Manager")
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Create widgets for managing websites."""

        frame = ttk.Frame(self.window, padding=10)
        frame.grid(sticky="nsew")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.listbox = tk.Listbox(frame, height=8)
        self.listbox.grid(row=0, column=0, columnspan=2, sticky="nsew")

        ttk.Label(frame, text="URL:").grid(row=1, column=0, sticky="w")
        self.entry = ttk.Entry(frame)
        self.entry.grid(row=1, column=1, sticky="ew")

        add_btn = ttk.Button(frame, text="Add", command=self._on_add_click)
        rm_btn = ttk.Button(frame, text="Remove", command=self._on_remove_click)
        add_btn.grid(row=2, column=0, pady=5, sticky="ew")
        rm_btn.grid(row=2, column=1, pady=5, sticky="ew")

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

    def _on_add_click(self) -> None:
        if not self.entry:
            return
        url = self.entry.get().strip()
        self.add_website(url)

    def _on_remove_click(self) -> None:
        if not self.listbox:
            return
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No website selected")
            return
        url = self.listbox.get(selection[0])
        self.remove_website(url)

    # -------------------------------------------------------------- Logic ---
    def _is_valid_url(self, url: str) -> bool:
        parsed = urlparse(url)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

    def add_website(self, url: str) -> None:
        """Add a website to the list of sites to scrape."""

        if not self._is_valid_url(url):
            messagebox.showerror("Invalid URL", "Please enter a valid URL.")
            return

        if url in self.websites:
            messagebox.showerror("Duplicate", "Website already exists.")
            return

        self.websites.append(url)
        if self.listbox is not None:
            self.listbox.insert(tk.END, url)
        messagebox.showinfo("Website Added", f"{url} added")

    def remove_website(self, url: str) -> None:
        """Remove a website from the scrape list."""

        if url not in self.websites:
            messagebox.showerror("Not Found", "Website not found.")
            return

        self.websites.remove(url)
        if self.listbox is not None:
            items = list(self.listbox.get(0, tk.END))
            for idx, item in enumerate(items):
                if item == url:
                    self.listbox.delete(idx)
                    break
        messagebox.showinfo("Website Removed", f"{url} removed")
