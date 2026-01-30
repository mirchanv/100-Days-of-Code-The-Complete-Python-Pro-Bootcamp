# 🔐 Caesar Cipher (Python)

## 📖 Description
This project is a command-line implementation of the classic **Caesar Cipher** encryption technique built using Python. The program allows users to **encode** or **decode** messages by shifting letters of the alphabet by a user-specified number. Non-alphabetic characters (spaces, numbers, symbols) remain unchanged. A custom ASCII logo is displayed when the program starts for visual appeal.

---

## 🎯 Objective
Encrypt and decrypt messages using the Caesar Cipher while practicing Python fundamentals such as loops, conditionals, and string manipulation.

---

## 🕹️ How the Program Works
1. The program displays an ASCII logo when it starts.
2. The user chooses whether to **encode** or **decode** a message.
3. The user enters the message and specifies the shift number.
4. Each letter in the message is shifted forward (for encoding) or backward (for decoding) by the shift number.
5. Non-alphabetic characters are preserved.
6. The program outputs the encrypted or decrypted message.
7. Users can repeat the process until they choose to exit.

---

## 🧠 Key Concepts Used
- **User Input Handling** (`input()`)
- **Loops** (`while` loop for repeating)
- **Conditional Statements** (`if`, `else`)
- **String Manipulation**
- **Modular Functions** (`caesar()` function for encoding/decoding)
- **List Operations** (`index()` and modular arithmetic for shifting)
- ASCII Art for program branding

---

## 🛠️ Technologies
- **Language:** Python 3  
- **Environment:** Command Line / Terminal  

---

## ▶️ How to Run
1. Ensure Python 3 is installed.
2. Place `caesar_cipher.py` and `art.py` in the same directory.
3. Run the program using:
   ```bash
   python caesar_cipher.py