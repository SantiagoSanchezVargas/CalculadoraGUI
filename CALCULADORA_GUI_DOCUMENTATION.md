# Calculadora GUI Documentation

## Overview
`calculadoraGUI.py` is a simple calculator application built with Python's Tkinter library. It provides a graphical user interface (GUI) for performing basic arithmetic operations including addition, subtraction, multiplication, and division.

## Features
- **Basic Arithmetic Operations**: Addition (+), subtraction (-), multiplication (*), and division (/)
- **Number Input**: Digits 0-9 and decimal point support
- **Clear Function**: Button to clear the current expression
- **Error Handling**: Gracefully handles invalid expressions
- **User-Friendly GUI**: Grid-based button layout similar to physical calculators

## Class Structure

### `CalculadoraApp`
Main application class that manages the calculator interface and logic.

#### Attributes
- `root` (tk.Tk): The root window of the Tkinter application
- `expression` (str): Stores the current mathematical expression being built
- `entry` (tk.Entry): Text display widget showing the current expression/result

#### Methods

##### `__init__(self, root)`
**Purpose**: Initializes the calculator application and sets up the GUI.

**Parameters**:
- `root` (tk.Tk): The root Tkinter window

**Functionality**:
1. Sets window title to "Calculadora"
2. Disables window resizing
3. Creates an Entry widget for displaying expressions
4. Creates a grid of calculator buttons:
   - **Row 1**: 7, 8, 9, /
   - **Row 2**: 4, 5, 6, *
   - **Row 3**: 1, 2, 3, -
   - **Row 4**: 0, ., =, +
   - **Row 5**: C (Clear)
5. Binds each button to the `on_button_click` method

##### `on_button_click(self, char)`
**Purpose**: Handles button click events and processes user input.

**Parameters**:
- `char` (str): The character/operator clicked by the user

**Functionality**:
- **'C' (Clear)**: Resets the expression and clears the display
- **'=' (Equals)**: 
  - Evaluates the current expression using Python's `eval()` function
  - Displays the result
  - Updates expression to the result for further calculations
  - Shows "Error" message if the expression is invalid
- **Other characters**: Appends the character to the expression and updates the display

## Usage

### Running the Application
```bash
python calculadoraGUI.py
```

### Example Calculations
1. **Addition**: Click 5 + 3 = → Result: 8
2. **Multiplication**: Click 4 * 7 = → Result: 28
3. **Decimal numbers**: Click 10 . 5 + 2 . 5 = → Result: 13.0

## Technical Details

### Dependencies
- `tkinter`: Python's standard GUI library (included with Python)

### GUI Layout
- **Entry Widget**: Positioned at row 0, spanning all 4 columns
  - Font: Arial, 24pt
  - Width: 16 characters
  - Text alignment: Right-justified
  - Border style: Ridge

- **Button Grid**: 5x4 grid starting from row 1
  - Font: Arial, 18pt
  - Size: 4 characters wide, 2 characters tall
  - Layout: Standard calculator keyboard layout

### Error Handling
The application uses a try-except block to catch evaluation errors:
- Invalid expressions display "Error" in the entry field
- The expression is reset to an empty string after an error
- This prevents cascading errors from malformed input

## Limitations & Considerations

1. **Security**: The use of `eval()` can pose security risks if user input isn't validated, though in this GUI context it's relatively safe
2. **Expression Chaining**: After showing a result, you can immediately start a new calculation or continue with operators
3. **No Parentheses Support**: The calculator doesn't provide parentheses buttons for complex expressions
4. **No History**: Previous calculations are not stored or displayed

## Possible Enhancements

1. **Add parentheses** for complex expression support
2. **Display calculation history** in a separate widget
3. **Add keyboard support** for number input and operators
4. **Implement more functions** (square root, percentage, etc.)
5. **Add memory functions** (M+, M-, MR, MC)
6. **Improve error messages** for specific error types

## Module Import Safety
The script is designed to be safely imported as a module. The GUI only launches when the script is executed directly (via the `if __name__ == '__main__':` guard), allowing other scripts to import the `CalculadoraApp` class without instantiating the GUI.

---
Generated: December 2, 2025
