# 💻 Digital Coffee Machine

## 📖 Project Overview
This project is an interactive **command-line Digital Coffee Machine simulator** built in Python.

The program allows users to order coffee drinks such as **espresso, latte, and cappuccino**, processes coin payments, checks available resources, provides change, and updates machine profit. It simulates the real-world logic of an automated coffee vending machine while reinforcing core programming concepts.

---

## 🎯 Learning Objectives
- Practice organizing logic using functions
- Understand state management using variables and dictionaries
- Apply conditional logic for decision making
- Work with loops to keep the machine running continuously
- Handle user input and simulate real-world transactions

---

## 🕹️ Key Features
- Menu-based coffee selection (espresso, latte, cappuccino)
- Resource availability checking before purchase
- Coin processing system (quarters, dimes, nickels, pennies)
- Transaction validation with refund handling
- Automatic change calculation (rounded to 2 decimal places)
- Resource deduction after successful purchase
- Profit tracking and report generation
- Hidden **“off”** command to shut down the machine

---

## 🧠 Key Concepts Covered
- Functions and modular program design
- Dictionaries for structured data storage
- Conditional statements (`if / elif / else`)
- While loops for continuous execution
- User input handling and validation
- Basic financial calculation and rounding
- Program state and resource management

---

## 🛠️ Technologies Used
- Python 3.x
- Python Standard Library
  - `sys`
- Custom module
  - `machine_data.py` (menu and resource data)

---

## 📌 How The "Digital Coffee Machine" Works
- The machine prompts the user to choose a drink (**espresso/latte/cappuccino**)
- The machine checks if enough **water, milk, and coffee** are available
- If resources are sufficient, the user inserts coins
- The machine verifies the payment:
  - Refunds money if insufficient
  - Provides change if excess is inserted
- After a successful transaction:
  - Resources are deducted
  - Profit is updated
  - The drink is prepared and served
- The user can type:
  - **report** → to view current resources and profit
  - **off** → to shut down the machine

---

## 📌 Purpose
The purpose of this project is to strengthen **core Python programming skills** by simulating a real-world system. It focuses on control flow, resource management, user interaction, and modular code design—essential foundations for building larger software applications.

---

## ✅ Outcome
By completing this project, the learner gains:
- Stronger understanding of program structure and logic
- Experience handling real-world style transactions
- Confidence working with dictionaries and functions
- A practical Python project suitable for a beginner portfolio

---

☕ *Order smart, manage resources, and enjoy coding in Python!*