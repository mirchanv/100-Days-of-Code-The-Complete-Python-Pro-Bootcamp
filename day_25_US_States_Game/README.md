# 🇺🇸 US States Guessing Game

An interactive Python game that tests your knowledge of US geography by challenging you to guess all 50 states.  
Built using Turtle graphics and Pandas for data handling.

---

## 🚀 Features

- 🗺 Interactive US map using Turtle graphics  
- ⌨️ User input to guess state names  
- 📍 Correct guesses displayed on the map in real-time  
- 📊 Tracks progress (e.g., "10/50 States Correct")  
- 📁 Generates a CSV file of missed states for learning  
- 🧠 Case-insensitive input handling  

---

## 🛠 Tech Stack

- Python 3  
- Turtle Graphics  
- Pandas (data handling)  

---

## 📂 Project Structure

    us-states-game/
    │
    ├── main.py               # Main game logic
    ├── 50_states.csv         # State names with x/y coordinates
    ├── blank_states_img.gif  # US map image
    ├── states_to_learn.csv   # Generated file for missed states
    └── README.md

---

## 🧠 How It Works

1. The game loads the US map using Turtle graphics  
2. State data (name + coordinates) is read using Pandas  
3. The user is prompted to guess a state name  
4. If the guess is correct:
   - The state name is displayed on the map at the correct coordinates  
   - It is added to the list of correct guesses  
5. The game continues until:
   - All 50 states are guessed, OR  
   - The user exits the game  

6. If the game ends early:
   - A file `states_to_learn.csv` is generated  
   - Contains all states the user missed  

---

## 🎯 Game Mechanics

- Input state names via a pop-up text prompt  
- Correct guesses appear visually on the map  
- Duplicate guesses are ignored  
- Typing `Exit` ends the game early  

---

## ⚙️ Key Concepts Used

- Data handling with Pandas (`read_csv`, filtering)  
- Turtle graphics for UI rendering  
- Event-driven user input (`textinput`)  
- List comparison and filtering  
- File output using CSV  

---
