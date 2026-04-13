# 📏 Miles to Kilometers Converter (Tkinter GUI)

A simple desktop application built with Python’s Tkinter library that converts miles to kilometers in real-time.

---

## 🚀 Features

- 🖥 Graphical User Interface (GUI) using Tkinter  
- 🔢 User input field for miles  
- ⚡ Instant conversion to kilometers on button click  
- 🧹 Automatically clears previous results before new conversion  
- 📢 Displays formatted output message  

---

## 🛠 Tech Stack

- Python 3  
- Tkinter (GUI library)  

---

## 📂 Project Structure

    mile-to-km-converter/
    │
    ├── main.py
    └── README.md

---

## 🧠 How It Works

1. The user enters a value in miles  
2. Clicks the **Convert** button  
3. The program:
   - Reads the input value  
   - Converts miles to kilometers using:
     ```
     km = miles × 1.609
     ```
   - Displays the result (rounded to 2 decimal places)  
   - Updates a label showing the full conversion  

---

## ⚙️ Core Functions

- `convert_mile_to_km()`  
  - Reads input  
  - Performs conversion  
  - Updates output field and label  

- `clear_km_field()`  
  - Clears previous result before new calculation  

- `display_output_text()`  
  - Displays formatted result:
    ```
    X miles is equal to Y kms
    ```

---

## 🎯 User Interface

- Entry field for miles input  
- Entry field for kilometers output  
- Convert button  
- Labels for units and result display  

---