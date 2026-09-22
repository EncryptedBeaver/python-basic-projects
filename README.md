# 🐍 Python Basic Projects

A collection of beginner-friendly Python projects created to practice fundamental programming concepts.

---

## 🎲 1. Guess the Number Game

### 📝 Description
A classic interactive CLI game where the program generates a random integer between **1 and 100** and prompts the user to guess it. 

* If the guess is higher than the secret number, the program outputs: `'Too high, try again'`.
* If the guess is lower than the secret number, the program outputs: `'Too low, try again'`.
* When guessed correctly, the program congratulates the user: `'You guessed it, congratulations!'`.

---

### 🛠️ Key Concepts Applied
This project demonstrates basic Python functionality and flow control:

* **Data Types:** Integers (`int`)
* **Variables:** Storing user inputs and generated numbers
* **I/O Operations:** Console input/output using `input()` and `print()`
* **Conditional Logic:** Branching with `if` / `elif` / `else`
* **Loops:** Repetition using `while` (and infinite loop patterns)
* **Loop Control:** Managing iteration state with `break` and `continue`
* **Standard Modules:** Random number generation via the `random` module

---


## 🎱 2. Magic 8 Ball

### 📝 Description
A fun command-line fortune-telling application. The program greets the user by name, prompts them to ask any question, and randomly selects a humorous or insightful response from a predefined list of answers.

---

### 🛠️ Key Concepts Applied
* **Data Types:** Strings (`str`), Integers (`int`), and Lists (`list`)
* **Variables & Lists:** Storing multiple prompt variations and answers in structured lists
* **I/O Operations:** Reading user input via `input()` and outputting answers with `print()`
* **String Methods:** Formatting text with `.capitalize()`, `.lower()`, `.strip()`, and `f-strings`
* **Custom Functions:** Reusable logic using `def` (e.g., `one_more_question()`)
* **Control Flow:** Validation and branching using `if` / `elif` / `else` logic
* **Loop Mechanics:** Infinite main loop (`while True`) managed with `break` and state conditions
* **Random Module:** Selecting dynamic elements using `random.choice()`

---

## 🔐 3. Password Generator

### 📝 Description
A customizable command-line tool that generates secure, random passwords based on user preferences. You can set the number of passwords, choose the length, and selectively include or exclude digits, uppercase/lowercase letters, and special symbols.

### 🛠️ Key Concepts Applied
* **Data Types & Variables:** Working with strings (`str`), integers (`int`), and boolean values (`True`/`False`).
* **I/O Operations:** Taking interactive prompts with `input()` and formatting the output via `print()`.
* **Input Sanitation:** Cleaning strings using `.strip()` and `.lower()` to handle user choices safely.
* **Reusable Functions:** Custom validation functions (`ask_question`, `ask_number`) to follow DRY principles and handle logic neatly.
* **Control Flow & Loops:** Input validation using `while` loops and batch generation using `for` loops.
* **Random Module:** Utilizing `random.sample()` / `random.choices()` to assemble unpredictable character strings.



### 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone the repository and navigate to the project directory:
   git clone [https://github.com/EncryptedBeaver/python-basic-projects.git](https://github.com/your-username/python-basic-projects.git)
   cd python-basic-projects
