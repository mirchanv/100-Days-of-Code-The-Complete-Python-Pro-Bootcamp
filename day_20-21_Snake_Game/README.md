# Classic Snake Game in Python

## Overview
This is a Python implementation of the classic old-school Snake game. The player controls a snake that moves around the screen to eat food and grow longer while avoiding collisions with the walls and itself.  

This project demonstrates Python programming fundamentals, Object-Oriented Programming (OOP), modular design, and real-time game logic using the `turtle` module.

**Technologies & Skills:**  
- Python 3.x  
- Object-Oriented Programming (OOP)  
- Turtle module for GUI  
- Game loop, collision detection, and event handling  

## Features
- Move snake in four directions using keyboard  
- Food spawns at random locations  
- Snake grows after eating food  
- Scoreboard tracks current score and high score  
- Game over on wall or self collision  

## Architecture
```mermaid
flowchart TD
    Main[main.py] --> Snake[snake.py]
    Main --> Food[food.py]
    Main --> Scoreboard[scoreboard.py]
    Snake --> Movement[Movement & Growth Logic]
    Food --> Spawn[Random Position Logic]
    Scoreboard --> Score[Update & Display Logic]