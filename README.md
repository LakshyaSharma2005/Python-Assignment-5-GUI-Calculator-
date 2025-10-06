# 🧮 Calculator App (Tkinter)

A simple and elegant **GUI Calculator** built using **Python’s Tkinter library**.
This calculator supports basic arithmetic operations along with percentage handling, delete, and clear functionalities — all wrapped in a clean UI.

---

## 🚀 Features

✅ Basic arithmetic operations — `+`, `-`, `x`, `/`
✅ Percentage calculations (`%`) with enhanced logic
✅ `C` (clear) and `del` (delete last character) functions
✅ Error handling for invalid expressions
✅ Read-only display to prevent unwanted edits
✅ Modern layout with clear, large buttons

---

## 🧩 How It Works

The calculator uses a single **event handler function (`calculator`)** that binds to all buttons.
When a button is clicked, the text from that button is fetched and evaluated through logic that:

1. Builds expressions dynamically.
2. Replaces `x` with `*` for Python’s evaluation.
3. Converts percentage (`%`) into valid mathematical expressions using regex.
4. Evaluates safely using `eval()` inside a `try-except` block.

---

## 🧠 Percentage Logic

The app supports expressions like:

| Expression | Interpreted As   | Result |
| ---------- | ---------------- | ------ |
| `50%`      | 50/100           | 0.5    |
| `10%100`   | (10/100) * 100   | 10     |
| `50+10%50` | 50 + (10/100)*50 | 55     |

This makes the percentage operation work more like a **real calculator**.

---

## 🖥️ UI Layout

* **Entry widget** (display): Shows the expression/result
* **Button grid (5x4)**: Number keys, operators, and function keys
* Color-coded buttons:

  * **Orange** → Operator or control (`C`, `%`, `/`, `x`, `-`, `+`, `=`)
  * **Gray** → Number buttons

---

## ⚙️ Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python)

---

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/tkinter-calculator.git
   ```
2. Navigate into the folder:

   ```bash
   cd tkinter-calculator
   ```
3. Run the script:

   ```bash
   python calculator.py
   ```

---

## 📸 Screenshot (Optional)

<img width="620" height="727" alt="image" src="https://github.com/user-attachments/assets/4eb021e5-6082-46d3-8e6a-da07cdeb121e" />


---

## 🧑‍💻 Author

**Your Name**
🔗 GitHub: [@your-username](https://github.com/your-username)
💬 Contributions, suggestions, and forks are welcome!

---

## 📜 License

This project is open-source and available under the **MIT License**.
