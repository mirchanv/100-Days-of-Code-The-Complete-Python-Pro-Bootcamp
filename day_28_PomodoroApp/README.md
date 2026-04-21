# 🍅 Pomodoro Timer App (Tkinter)

A clean and minimal **Pomodoro Timer desktop application** built using **Python and Tkinter**.  
This app helps improve focus and productivity using the **Pomodoro Technique** by automating work and break cycles with a simple and responsive UI.

---

## 🚀 Features

- ⏱️ Pomodoro (Work), Short Break, and Long Break cycles
- 🔄 Automatic session transitions based on repetition count
- 🎯 Visual progress tracking using emoji indicators
- 🎨 Dynamic UI color changes based on current mode
- 🖱️ Interactive buttons with hover effects
- 🔒 Prevents multiple timer instances from running simultaneously
- 🔔 Audible alert when a session ends
- 🔁 Reset functionality to restart the entire timer

---

## 🧠 How It Works

The timer follows a structured Pomodoro cycle:

1. Pomodoro (Work Session)
2. Short Break
3. Repeat
4. After 4 work sessions → Long Break

### Internal Logic:
- Odd reps → Pomodoro  
- Even reps → Short Break  
- Every 9th rep → Long Break  

---

## 🏗️ Project Structure

```
pomodoro-timer/
│
├── main.py          # Complete application logic and UI
└── README.md        # Project documentation
```

---

## ⚙️ Tech Stack

- Python 3  
- Tkinter (GUI Framework)  
- Math module  

---

## 🎨 UI Overview

- Dark-themed interface for better focus  
- Mode-based color system:
  - 🩷 Pomodoro → Pink  
  - 🟢 Short Break → Green  
  - 🟡 Long Break → Yellow  

### Progress Tracking:
- ⭕ = Incomplete session  
- 🔴 = Completed session  

---

## ▶️ How to Run

1. Ensure Python 3 is installed  
2. Save the code in a file named `main.py`  
3. Run the application:

```bash
python main.py
```

---

## 🛠️ Customization

You can adjust session durations:

```
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

---

## 📌 Key Learnings

- Implementing asynchronous timers using Tkinter’s `.after()` method  
- Avoiding UI blocking by eliminating traditional loops  
- Managing application state using global variables  
- Structuring event-driven applications  
- Creating reusable UI behaviors (hover effects, button interactions)  
- Handling edge cases like multiple button clicks and timer overlap  
- Working around Tkinter styling limitations  

---

## 🚧 Future Improvements

- ⏸ Pause and Resume functionality  
- 🔊 Custom sound notifications  
- 📊 Session tracking and analytics  
- 💾 Save progress locally  
- 🎨 Enhanced UI  
---
