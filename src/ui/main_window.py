"""Main application window."""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
import os

zodiac_signs = [
    ("Capricorn", (1, 19)),
    ("Aquarius", (2, 18)),
    ("Pisces", (3, 20)),
    ("Aries", (4, 19)),
    ("Taurus", (5, 20)),
    ("Gemini", (6, 20)),
    ("Cancer", (7, 22)),
    ("Leo", (8, 22)),
    ("Virgo", (9, 22)),
    ("Libra", (10, 22)),
    ("Scorpio", (11, 21)),
    ("Sagittarius", (12, 21)),
    ("Capricorn", (12, 31))
]

common_text_format = {
    "background": "#ffffff",
}

class MainWindow:
    """Main application window for Zodiac Finder."""
    
    def __init__(self, window):
        """
        Initialize the main window.
        
        Args:
            window: The tkinter window window
        """
        self.window = window
        self.current_image = None
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Configure the main window."""
        self.window.title("ZodiacPy - Trova il tuo segno Zodiacale")
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        
        self.window.configure(bg="#ffffff")
    
    def create_widgets(self):
        """Create and layout all widgets."""
        # Title Frame
        title_frame = tk.Frame(self.window, bg="#ffffff")
        title_frame.pack(pady=20, padx=20, fill=tk.X)
        
        title_label = ttk.Label(
            title_frame,
            text="Ottieni il tuo segno Zodiacale",
            font=("Helvetica", 16, "bold"),
            background=common_text_format.get("background")
        )
        title_label.pack(anchor="center")
        
        # Instructions Frame
        instructions_frame = tk.Frame(self.window, bg="#ffffff")
        instructions_frame.pack(pady=10, padx=20, fill=tk.X)
        
        instructions_label = ttk.Label(
            instructions_frame,
            text="Inserisci la data di nascita:",
            font=("Helvetica", 12),
            background=common_text_format.get("background")
        )
        instructions_label.pack(anchor="w")
        
        # Date Inputs Frame
        inputs_frame = tk.Frame(self.window, bg="#ffffff")
        inputs_frame.pack(pady=10, padx=20, fill=tk.X)
        
        month_frame = tk.Frame(inputs_frame, bg="#ffffff")
        month_frame.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(
            month_frame,
            text="Mese:",
            background=common_text_format.get("background")
        ).pack()
        
        self.month_var = tk.StringVar()
        month_spinbox = ttk.Spinbox(
            month_frame,
            from_=1,
            to=12,
            textvariable=self.month_var,
            width=5
        )
        month_spinbox.pack()
        
        day_frame = tk.Frame(inputs_frame, bg="#ffffff")
        day_frame.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(
            day_frame,
            text="Giorno:",
            background=common_text_format.get("background")
        ).pack()
        
        self.day_var = tk.StringVar()
        day_spinbox = ttk.Spinbox(
            day_frame,
            from_=1,
            to=31,
            textvariable=self.day_var,
            width=5
        )
        day_spinbox.pack()
        
        # Button Frame
        button_frame = tk.Frame(self.window, bg="#ffffff")
        button_frame.pack(pady=20)
        
        find_button = ttk.Button(
            button_frame,
            text="Calcola il segno Zodiacale",
            command=self.find_zodiac
        )
        find_button.pack()
        
        # Result Label Frame
        result_frame = tk.Frame(self.window, bg="#ffffff")
        result_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.result_label = ttk.Label(
            result_frame,
            text="",
            font=("Helvetica", 12),
            foreground="blue",
            background=common_text_format.get("background")
        )
        self.result_label.pack(anchor="w")
        
        # Image Frame
        image_frame = tk.Frame(self.window, bg="#ffffff")
        image_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.image_label = ttk.Label(image_frame, background=common_text_format.get("background"))
        self.image_label.pack()
        
        self.month_var.set("1")
        self.day_var.set("1")
    
    def find_zodiac(self):
        """Find and display the zodiac sign for the entered date."""
        try:
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            
            if month < 1 or month > 12 or day < 1 or day > 31:
                self.image_label.config(image="")
                self.current_image = None
                return
            
            zodiac_sign = self.get_zodiac_sign(month, day)
            self.result_label.config(
                text=f"Il tuo segno zodiacale è: {zodiac_sign}",
                foreground="green"
            )
            self.load_zodiac_image(zodiac_sign)
        except ValueError:
            self.result_label.config(
                text="Please enter valid numbers.",
                foreground="red"
            )
            self.image_label.config(image="")
            self.current_image = None
            self.result_label.config(
                text="Please enter valid numbers.",
                foreground="red"
            )
    
    @staticmethod
    def get_zodiac_sign(month, day):
        """
        Get the zodiac sign for a given date.
        
        Args:
            month: Birth month (1-12)
            day: Birth day (1-31)
            
        Returns:
            The zodiac sign as a string
        """
        
        for sign, (sign_month, sign_day) in zodiac_signs:
            if month == sign_month and day <= sign_day:
                return sign
        
        return "Capricorn"
    
    def load_zodiac_image(self, zodiac_sign):
        """
        Load and display the zodiac sign image.
        
        Args:
            zodiac_sign: The name of the zodiac sign
        """
        # Get the assets directory path
        assets_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')
        image_path = os.path.join(assets_dir, f"{zodiac_sign.lower()}.png")
        
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                # Resize image to fit the window (200x200)
                image.thumbnail((400, 400), Image.Resampling.LANCZOS)
                self.current_image = ImageTk.PhotoImage(image)
                self.image_label.config(image=self.current_image)
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            # No image found
            self.image_label.config(image="")
