# 💻 Hirst Dot Painting Generator (Python Turtle)

## 📖 Project Overview
This project recreates a digital version of a **Damien Hirst-inspired dot painting** using Python’s Turtle graphics module.

The program generates a 10x10 grid of colored dots, randomly selecting colors extracted from an image using the `colorgram` module. The result is a vibrant, algorithmically generated artwork inspired by Hirst’s iconic spot paintings.

The project combines creative coding with Python fundamentals, randomness, loops, coordinate positioning, and color manipulation.

---

## 🎯 Learning Objectives
- Work with the Turtle graphics module
- Understand coordinate positioning in 2D space
- Practice nested loops
- Apply randomness in visual output
- Use RGB color mode in Python
- Extract and use color palettes from images
- Build a generative art project

---

## 🕹️ Key Features
- Generates a 10x10 dot grid
- Uses RGB color mode (0–255)
- Randomly selects colors from a predefined palette
- Fast rendering using `speed("fastest")`
- Clean layout using `penup()` and manual positioning
- Inspired by Damien Hirst’s dot paintings
- Colors extracted from `image.jpg` using `colorgram`

---

## 🧠 Key Concepts Covered
- Nested loops
- Constants for configuration
- Turtle coordinate system
- RGB color tuples
- Random selection with `random.choice()`
- Modular function design
- Screen setup and rendering control

---

## 🛠️ Technologies Used
- Python 3.x
- Turtle graphics module
- Random module
- Colorgram module (for palette extraction)

Example of color extraction:

```python
import colorgram

colors = colorgram.extract("image.jpg", 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))
```