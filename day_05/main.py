import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_list = []
strong_pwd = ""

# Generate random letters
for i in range(0, nr_letters):
    pwd_list.append(random.choice(letters))

# Generate random symbols
for i in range(0, nr_symbols):
    pwd_list.append(random.choice(symbols))

# Generate random numbers
for i in range(0, nr_numbers):
    pwd_list.append(random.choice(numbers))

print("pwd_list :", pwd_list)

# shuffle the items in the list
random.shuffle(pwd_list)

for char in pwd_list:
    strong_pwd += char

print(f"Your password is: {strong_pwd}")
