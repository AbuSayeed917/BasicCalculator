
import tkinter as tk

class ModernCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Basic Calculator")
        self.window.geometry("500x400")
        self.window.resizable(True,True)

        self.current = ""
        self.expression = ""

        # Display
        self.display = tk.Label(self.window, text="0", anchor="e", height=10, bg="white")
        self.display.pack(fill="x")

        # Buttons frame
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack(expand=True, fill="both")

        # Buttons
        self.buttons = {
            'AC': (0, 0), '±': (0, 1), '%': (0, 2), '÷': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '×': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3),
            '0': (4, 0), '.': (4, 1), '=': (4, 3)
        }

        self.create_buttons()

    def create_buttons(self):
        for text, (row, col) in self.buttons.items():
            button = tk.Button(self.buttons_frame, text=text, command=lambda x=text: self.button_click(x))
            button.grid(row=row, column=col, sticky="nsew")

        # Adjust grid weights
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == "AC":
            self.current = ""
            self.expression = ""
        elif value == "=":
            try:
                self.expression += self.current
                result = eval(self.expression.replace('×', '*').replace('÷', '/'))
                self.current = str(result)
                self.expression = ""
            except:
                self.current = "Error"
                self.expression = ""
        elif value == "±":
            if self.current and self.current != "Error":
                self.current = self.current[1:] if self.current[0] == '-' else '-' + self.current
        elif value == "%":
            if self.current and self.current != "Error":
                try:
                    self.current = str(float(self.current) / 100)
                except:
                    self.current = "Error"
        else:
            self.current += value

        self.update_display()

    def update_display(self):
        self.display.config(text=self.current if self.current else "0")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = BasicCalculator()
    calculator.run()
