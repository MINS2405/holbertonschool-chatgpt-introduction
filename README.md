# 🤖✨ ChatGPT Introduction Project ✨🤖

<div align="center">
  <img src="https://img.icons8.com/color/96/000000/artificial-intelligence.png" width="80" alt="AI Icon"/>
  <img src="https://img.icons8.com/fluency/96/000000/chatgpt.png" width="80" alt="ChatGPT Icon"/>
</div>

---

Welcome to the **ChatGPT Introduction Project**!  
This repository shows how to use ChatGPT and AI tools to debug code, automate tasks, and improve your programming skills.  
Perfect for beginners and anyone curious about AI in development! 🚀😊

---

## 🌟 Overview

With this project, you will learn how to:

- **Debug code** with ChatGPT’s help
- **Automate repetitive tasks** (like documentation)
- **Write clear comments and docstrings**

---

## 🗂️ Project Structure

| File/Folder                        | Description                             |
|-------------------------------------|-----------------------------------------|
| `debugging/factorial.py`            | Fix a Python factorial function         |
| `debugging/print_arguments.py`      | Print command-line arguments            |
| `debugging/change_background.html`  | Change background color with JS         |
| `debugging/mines.py`                | Debug a Python Minesweeper game         |
| `debugging/factorial_recursive.py`  | Add docstrings to recursive factorial   |
| `debugging/checkbook.py`            | Add error handling to a checkbook app   |
| `debugging/tic.py`                  | Fix a Python Tic Tac Toe game           |

---

## 🚀 Getting Started

1. **Clone the repository**

git clone https://github.com/your-username/chatgpt-introduction.git
cd chatgpt-introduction


2. **Explore the code**
Open the `debugging/` folder and try to run and fix the scripts.

3. **Test your solutions**
Example:

python3 debugging/factorial.py 5


---

## 💡 Example Code

### factorial.py

#!/usr/bin/python3
import sys

def factorial(n):
result = 1
while n > 1:
result *= n
n -= 1 # Correct: decrement n!
return result

if name == "main":
f = factorial(int(sys.argv))
print(f)


---

### print_arguments.py

#!/usr/bin/python3
import sys

for arg in sys.argv[1:]:
print(arg)


---

### change_background.html

<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>Change Background Color</title> </head> <body> <h2>Click the button to change the background color</h2> <button id="colorButton">Change Color</button> <script> document.getElementById("colorButton").addEventListener("click", function() { var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16); document.body.style.backgroundColor = randomColor; }); </script> </body> </html> ```

factorial_recursive.py

#!/usr/bin/python3
def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Args:
        n (int): The number to calculate factorial for.

    Returns:
        int: The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

checkbook.py

#!/usr/bin/python3
def withdraw(balance, amount):
    try:
        amount = float(amount)
        if amount > balance:
            print("Insufficient funds.")
            return balance
        return balance - amount
    except ValueError:
        print("Invalid amount.")
        return balance

tic.py

#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row == row == row and row != " ":
            return row
    # Check columns
    for col in range(3):
        if board[col] == board[col] == board[col] and board[col] != " ":
            return board[col]
    # Check diagonals
    if board == board == board and board != " ":
        return board
    if board == board == board and board != " ":
        return board
    return None

# Example usage
board =
         ["X", "O", "X"],

         ["O", "X", "O"],
         
         ["O", "X", "X"]]
         
print_board(board)
winner = check_winner(board)
if winner:
    print("Winner:", winner)
else:
    print("No winner.")



## 😃 Tips
* Always test the code after fixing it.

* Use ChatGPT to help you understand errors and improve your code.

* Comment your code for better readability.

## 🤝 Contributing
* Contributions are welcome!
* Feel free to open issues or pull requests.

## 🛡️ License
* This project is licensed under the MIT License.

<div align="center"> <h3>Happy coding and AI learning! 🤖💻✨</h3> </div> ```
