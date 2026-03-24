# 🐍 Snake Game (Classic Arcade)

A classic **Snake Game** built using Python’s Turtle graphics module.  
Control the snake, eat food to grow longer, and avoid colliding with walls or yourself.

---

## 🚀 Features

- 🐍 Smooth snake movement using keyboard controls
- 🍎 Randomly spawning food
- 📈 Score tracking system
- 💾 Persistent high score
- 🧠 Object-Oriented Design (OOP)
- 🖥 Real-time animation using Turtle graphics
- 💥 Collision detection (walls & self)

---

## 🛠 Tech Stack

- Python 3
- Turtle Graphics Module
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

    snake-game/
    │
    ├── main.py        # Game loop and controller
    ├── snake.py       # Snake movement & behavior
    ├── food.py        # Food spawning logic
    ├── scoreboard.py  # Score tracking & display
    └── README.md

---

## 🧠 How It Works

### Game Loop (`main.py`)
- Runs the main game loop
- Updates screen continuously
- Detects collisions (wall, food, self)
- Controls game speed

---

### Snake (`snake.py`)
- Handles snake creation and movement
- Controls direction (Up, Down, Left, Right)
- Extends snake when food is eaten

---

### Food (`food.py`)
- Generates food at random positions
- Refreshes location after being eaten

---

### Scoreboard (`scoreboard.py`)
- Displays current score
- Updates score when food is eaten
- Handles game over and high score logic

---

## 🎯 Game Mechanics

- Use **Arrow Keys** to control the snake:
  - ↑ Up
  - ↓ Down
  - ← Left
  - → Right
- Eat food to grow longer
- Avoid:
  - Hitting the wall
  - Hitting yourself
- Game restarts on collision

---

## ⚠️ Future Improvements

- Add levels (increase speed over time)
- Add sound effects
- Improve UI (start screen / restart option)
- Add pause functionality
- Add obstacles

---

## 💡 Key Learning Outcomes

- Object-Oriented Programming (OOP)
- Game loop design
- Event handling (keyboard input)
- Collision detection
- Working with animations in Python

---
