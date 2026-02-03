import random
from art import logo

def generate_random_number():
    return random.randint(1, 100)

def set_guesses(level):
    if level == "easy":
        return 10
    else:
        return 5

def too_high():
    print("Too high 📈\nGuess again.")

def too_low():
    print("Too low 📉\nGuess again.")

print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")

NUMBER_TO_GUESS = generate_random_number()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guesses_left = set_guesses(difficulty)

guessed_correctly = False

while guesses_left > 0 and not guessed_correctly:
    print(f"You have {guesses_left} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))

    if player_guess == NUMBER_TO_GUESS:
        print(f"You got it! The answer was {NUMBER_TO_GUESS} 😎")
        guessed_correctly = True
    elif player_guess > NUMBER_TO_GUESS and guesses_left > 1:
        too_high()
        guesses_left -= 1
    elif player_guess < NUMBER_TO_GUESS and guesses_left > 1:
        too_low()
        guesses_left -= 1
    else:
        print("You've run out of guesses.")
        guesses_left -= 1

if not guessed_correctly:
    print(f"YOU LOST 😭 The number was: {NUMBER_TO_GUESS}")
