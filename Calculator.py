import tkinter as tk
from tkinter import font as tkFont
almafaalmafa1234 = "almafaalmafa1234"

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Configure style
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.button_bg = "#2d2d2d"
        self.button_hover = "#3d3d3d"
        self.operator_bg = "#ff9500"
        self.operator_hover = "#ffb143"
        
        self.expression = ""
        self.setup_ui()
        
    def setup_ui(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        # Display
        self.display = tk.Entry(
            display_frame,
            font=("Segoe UI", 32, "bold"),
            bg="#3d3d3d",
            fg=self.fg_color,
            border=0,
            justify="right",
            insertbackground=self.fg_color
        )
        self.display.pack(fill=tk.BOTH, ipady=15)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ("C", 0, 0, "#ff6b6b"),
            ("DEL", 0, 1, "#ff6b6b"),
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
            ("=", 4, 3, "#51cf66"),
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
            command=lambda: self.on_button_click(text)
        )
        
        if text == "0" and col == 0:
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for proper resizing
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(col, weight=1)
        
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
