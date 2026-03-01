# 🎨 Etch A Sketch App

## 📖 Project Overview
This project is an interactive drawing application built using Python’s Turtle graphics module.

The application allows users to control turtle movement using arrow keys while dynamically controlling drawing behavior through keyboard events. Drawing mode is activated when the spacebar is pressed and deactivated when it is released, demonstrating real-time event handling.

The project showcases event-driven programming principles, keyboard input handling, and state-based behavior management in a graphical environment.

---

## 🎯 Learning Objectives
- Understand event-driven programming
- Work with keyboard listeners (`onkeypress`, `onkeyrelease`)
- Manage drawing state dynamically
- Separate movement logic from drawing logic
- Control Turtle graphics behavior interactively
- Strengthen architectural thinking in small applications

---

## 🕹️ Key Features
- Arrow key movement control
- Drawing mode activated via spacebar press
- Drawing mode disabled on spacebar release
- Fast rendering using `speed("fastest")`
- Canvas reset functionality
- Clean separation of responsibilities

---

## 🧠 Key Concepts Covered
- Event binding with `Screen.onkeypress()`
- Event binding with `Screen.onkeyrelease()`
- Boolean state management
- Pen control (`penup()` / `pendown()`)
- Movement abstraction using constants
- Interactive graphical UI design

---

## 🛠️ Technologies Used
- Python 3.x
- Turtle graphics module
- Event-driven programming model

---

## 📂 Project Structure

    event_driven_turtle_app/
    │
    ├── main.py
    └── README.md

---

## 🧩 Architecture Overview
The application follows a simple layered design:

### 1️⃣ Configuration Layer
- `MOVE_DISTANCE` constant
- `TURN_ANGLE` constant
- Initial turtle configuration

### 2️⃣ Behavior Layer
- Movement functions (forward, backward, turn)
- Drawing control functions (enable / disable drawing)
- Screen reset function

### 3️⃣ Event Binding Layer
- Arrow keys mapped to movement
- Spacebar press → drawing enabled
- Spacebar release → drawing disabled
- 'C' key → reset canvas

This separation keeps the logic modular and easy to extend.

---

## 🎮 Controls

| Key       | Action                        |
|-----------|--------------------------------|
| ↑         | Move forward                   |
| ↓         | Move backward                  |
| ←         | Turn left                      |
| →         | Turn right                     |
| Space     | Hold to enable drawing         |
| C         | Reset canvas                   |

---

## 📌 Purpose
The purpose of this project is to demonstrate interactive graphical programming using real-time keyboard input.

It introduces state-based behavior control and event-driven architecture — foundational concepts in GUI applications, game development, and modern software systems.

---

## 🚀 Potential Improvements
- Convert to object-oriented structure
- Add drawing mode indicator on screen
- Add color selection via keyboard
- Add brush thickness control
- Implement smooth continuous movement
- Add undo functionality
- Allow saving drawings as image files

---

## ✅ Outcome
By completing this project, the learner gains:

- Hands-on experience with event-driven systems
- Deeper understanding of UI state control
- Improved separation of logic and input handling
- Confidence working with graphical libraries
- A clean, interactive Python portfolio project

---

🎮 Event-driven logic meets interactive design.