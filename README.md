🧮 Calculator App (Tkinter)

A simple calculator application built using Python Tkinter GUI library. This app supports basic arithmetic operations with a user-friendly interface.

📌 Features

Basic operations: Addition, Subtraction, Multiplication, Division

Extra functions: Clear (C), Delete (del), Decimal point (.)

Entry field for displaying current expression/result

Error handling for invalid expressions

GUI styled with Tkinter Button and Entry widgets

📂 Project Structure calculator.py # Main Python script

▶️ How to Run

Make sure you have Python 3 installed. Check version:

python --version

Save the script as calculator.py.

Run the program:

python calculator.py

🎨 GUI Layout

Top: Entry box to display current input/expression

Buttons arranged in a grid:

Row 2: C, %, del, /

Row 3: 7, 8, 9, x

Row 4: 4, 5, 6, -

Row 5: 1, 2, 3, +

Row 6: 00, 0, ., =

⚙️ Key Functions

calculator(event) Handles button clicks:

"=": Evaluates expression using eval()

"C": Clears the input

"del": Deletes last character

Other buttons: Appends to current expression

📷 Screenshot (Example UI)

image
🚀 Future Improvements

Add scientific functions (sin, cos, sqrt, log, etc.)

Keyboard input support

Dark mode theme

Memory functions (M+, M-, MR)
