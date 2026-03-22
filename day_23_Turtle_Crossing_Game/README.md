# 🐢 Turtle Crossing Game

A classic arcade-style **Frogger-inspired game** built using Python’s Turtle graphics module.  
Guide the turtle safely across the road while avoiding incoming cars that increase in speed with each level.

---

## 🚀 Features

- 🐢 Player-controlled turtle movement
- 🚗 Dynamic car generation with random colors and positions
- 📈 Progressive difficulty (cars increase speed each level)
- 🧠 Object-Oriented Design (OOP)
- 🖥 Real-time animation using Turtle graphics
- 📊 Level tracking system

---

## 🛠 Tech Stack

- Python 3
- Turtle Graphics Module
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

    turtle-crossing-game/
    │
    ├── main.py          # Game loop and controller
    ├── player.py        # Player (turtle) logic
    ├── car_manager.py   # Car generation & movement
    ├── scoreboard.py    # UI and level tracking
    └── README.md

---

## 🧠 How It Works

### Game Loop (`main.py`)
- Runs the main game loop
- Generates cars
- Moves all cars
- Handles level progression
- Detect collision with car

---

### Player (`player.py`)
- Moves upward on key press
- Detects level completion
- Resets position after reaching the finish line

---

### Car Manager (`car_manager.py`)
- Spawns cars at intervals
- Moves cars across the screen
- Increases speed as levels progress

---

### Scoreboard (`scoreboard.py`)
- Displays current level
- Updates the UI dynamically

---

## 🎯 Game Mechanics

- Press **↑ (Up Arrow)** to move forward
- Reach the top to level up
- Each level increases car speed

---

## 💡 Key Learning Outcomes

- Object-Oriented Programming (OOP)
- Game loop design
- Working with animations in Python
- Managing multiple objects in real-time

---