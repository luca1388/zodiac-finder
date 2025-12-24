#!/usr/bin/env python3
"""
Main entry point for the Zodiac Finder application.
"""

import tkinter as tk
from src.ui.main_window import MainWindow


def main():
    """Initialize and run the application."""
    window = tk.Tk()
    MainWindow(window)
    window.mainloop()


if __name__ == "__main__":
    main()
