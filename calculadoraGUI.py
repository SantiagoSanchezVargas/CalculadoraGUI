"""Simple Calculadora GUI using Tkinter.

Click buttons to perform basic arithmetic operations. From 0-9 digits to
addition, subtraction, multiplication, and division. The module exposes the
calculator logic functions so it can be imported safely (GUI only opens
when run as a script).
"""
import tkinter as tk

class CalculadoraApp: 
    def __init__(self, root):
        self.root = root
        root.title('Calculadora')
        root.resizable(False, False)

        self.expression = ""

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=4, height=2,
                               font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()