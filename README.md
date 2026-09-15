# Python Basic Projects

A collection of interactive command-line interface (CLI) applications built while mastering Python fundamentals, code architecture, PEP 8 standards, and input validation.

---

## 📌 Projects Included

### 1. Number Guessing Game (`guess_number.py`)
* **Description:** A CLI application where the program generates a random number and prompts the user to guess it, providing real-time feedback on whether the target number is higher or lower.
* **Core Concepts & Features:**
  * **Data Types & Variables:** Type conversion using `int` and variable scoping.
  * **I/O & String Formatting:** User input handling (`input()`), console output (`print()`), and formatted string literals (`f-strings`).
  * **Control Flow:** Conditional branching (`if`/`elif`/`else`) and nested control loops (`while True`).
  * **Loop Control:** Logic flow termination and skipping using `break`, `continue`, and `sys.exit()`.
  * **Input Validation & Helper Functions:** Reusable validation functions using `.isdigit()`, range checking, and string sanitation (`.strip().lower()`).
  * **Standard Modules:** Pseudo-random number generation via `random.randint()` and `random.choice()`.

### 2. Magic 8-Ball (`magic_ball.py`)
* **Description:** A digital fortune-telling tool that prompts the user for questions and returns randomized answers from a pre-defined list.
* **Core Concepts & Features:**
  * **Data Structures:** Multi-element sequence storage using Python lists (`list`).
  * **Randomization:** Selecting random elements from iterable collections via `random.choice()`.
  * **Modular Design:** Functions returning boolean values (`True`/`False`) to drive main execution loops.
  * **User Experience & Sanitation:** Dynamic multi-prompt strings and input cleaning using `.strip()` and `.lower()`.
  * **Clean Execution:** Game-state loops with early return patterns and exit options.

---

## 🛠️ Requirements & Setup

* **Python 3.x** (Standard library only; no external package installation needed).

To run any script locally, execute:
```bash
python <script_name>.py
