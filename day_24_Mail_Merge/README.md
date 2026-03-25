# 📧 Mail Merge Automation (Python)

A Python-based file automation project that generates personalized invitation letters using a template and a list of names.

---

## 🚀 Features

- 📄 Reads names from a text file  
- 📝 Uses a template letter with placeholders  
- 🔄 Replaces `[name]` with actual names  
- 📂 Generates personalized letters automatically  
- 💾 Saves output files to a designated folder  

---

## 🛠 Tech Stack

- Python 3  
- File Handling (read/write operations)  
- String Manipulation  

---

## 📂 Project Structure

    mail-merge-project/
    │
    ├── main.py
    ├── Input/
    │   ├── Names/
    │   │   └── invited_names.txt
    │   └── Letters/
    │       └── starting_letter.txt
    │
    ├── Output/
    │   └── ReadyToSend/
    │
    └── README.md

---

## 🧠 How It Works

1. The program reads all names from:
   Input/Names/invited_names.txt

2. It loads a letter template from:
   Input/Letters/starting_letter.txt

3. For each name:
   - Removes extra spaces using `strip()`
   - Replaces `[name]` in the template
   - Creates a personalized message

4. Saves each letter as:
   Output/ReadyToSend/letter_for_<name>

---

## ⚙️ Core Functions

- `read_names()` → Reads all names from file  
- `read_starting_letter()` → Loads template letter  
- `update_letter(content, guest)` → Replaces placeholder  
- `send_letter(message, guest)` → Writes output file  

---

## ▶️ How to Run

```bash
python main.py