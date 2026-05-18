import tkinter as tk
from tkinter import font as tkFont

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0a1428")
        
        # Configure style - Blue and Red Modern Theme
        self.bg_color = "#0a1428"  # Dark blue background
        self.fg_color = "#ffffff"  # White text
        self.button_bg = "#1e40af"  # Blue for numbers
        self.button_hover = "#1e3a8a"  # Darker blue
        self.operator_bg = "#dc2626"  # Red for operators
        self.operator_hover = "#b91c1c"  # Darker red
        self.accent_blue = "#3b82f6"  # Bright blue accent
        self.accent_red = "#ef4444"  # Bright red accent
        
        self.expression = ""
        self._create_background()
        self.setup_ui()
    
    def _create_background(self):
        """Create decorative background with gradient-like effect"""
        # Create decorative frames instead of canvas
        top_accent = tk.Frame(self.root, bg=self.accent_blue, height=3)
        top_accent.pack(side=tk.TOP, fill=tk.X)
        
        bottom_accent = tk.Frame(self.root, bg=self.accent_red, height=3)
        bottom_accent.pack(side=tk.BOTTOM, fill=tk.X)
        
    def setup_ui(self):
        # Display frame with blue border accent
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        # Border accent
        border = tk.Frame(display_frame, bg=self.accent_blue, height=2)
        border.pack(fill=tk.X, pady=(0, 8))
        
        # Display
        self.display = tk.Entry(
            display_frame,
            font=("Segoe UI", 32, "bold"),
            bg="#1e40af",
            fg=self.fg_color,
            border=0,
            justify="right",
            insertbackground=self.accent_blue
        )
        self.display.pack(fill=tk.BOTH, ipady=15)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ("C", 0, 0, self.operator_bg),
            ("DEL", 0, 1, self.operator_bg),
            ("%", 0, 2, self.operator_bg),
            ("÷", 0, 3, self.operator_bg),
            
            ("7", 1, 0, self.button_bg),
            ("8", 1, 1, self.button_bg),
            ("9", 1, 2, self.button_bg),
            ("×", 1, 3, self.operator_bg),
            
            ("4", 2, 0, self.button_bg),
            ("5", 2, 1, self.button_bg),
            ("6", 2, 2, self.button_bg),
            ("-", 2, 3, self.operator_bg),
            
            ("1", 3, 0, self.button_bg),
            ("2", 3, 1, self.button_bg),
            ("3", 3, 2, self.button_bg),
            ("+", 3, 3, self.operator_bg),
            
            ("0", 4, 0, self.button_bg),
            (".", 4, 2, self.button_bg),
            ("=", 4, 3, self.accent_red),
        ]
        
        for (text, row, col, color) in buttons:
            self.create_button(buttons_frame, text, row, col, color)
            
    def create_button(self, frame, text, row, col, color):
        btn = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 18, "bold"),
            bg=color,
            fg=self.fg_color,
            border=0,
            activebackground=color,
            activeforeground=self.fg_color,
            cursor="hand2",
            command=lambda: self.on_button_click(text),
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0,
            padx=0,
            pady=0
        )
        
        if text == "0" and col == 0:
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for proper resizing
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(col, weight=1)
        
        # Add hover effect
        btn.bind("<Enter>", lambda e: self._on_enter(btn, color))
        btn.bind("<Leave>", lambda e: self._on_leave(btn, color))
    
    def _on_enter(self, btn, original_color):
        """Brighten button on hover"""
        lighter_color = self.accent_blue if original_color == self.button_bg else self.accent_red if original_color in [self.operator_bg, self.accent_red] else original_color
        btn.config(bg=lighter_color)
    
    def _on_leave(self, btn, original_color):
        """Return button to original color"""
        btn.config(bg=original_color)
        
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "DEL":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        elif char == "=":
            try:
                # Replace symbols with Python operators
                calc_expr = self.expression.replace("×", "*").replace("÷", "/")
                result = eval(calc_expr)
                self.expression = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()
