import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = ["rock", "paper", "scissors"]
ascii_art = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer = choices.index(random.choice(choices))

if player >= 0 and player <= 2:
    print(f"You chose: {choices[player]} \n{ascii_art[player]}")
    print(f"Computer chose: {choices[computer]} \n{ascii_art[computer]}")
    if player == computer:
        print("It's a draw")
    elif player == 0 and computer != 1:
        print("You win, computer looses!")
    elif player == 0 and computer != 2:
        print("You lose, computer wins!")
    elif player == 1 and computer != 2:
        print("You win, computer looses!")
    elif player == 1 and computer != 1:
        print("You lose, computer wins!")
    elif player == 2 and computer != 0:
        print("You win, computer looses!")
    elif player == 2 and computer != 1:
        print("You lose, computer wins!")
else:
    print("Invalid choice!")
