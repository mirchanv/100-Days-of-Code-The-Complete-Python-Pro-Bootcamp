print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? "
                  "\nType \"left\" or \"right\": ").lower()

if direction == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. "
                   "\nType \"wait\" to wait for boat. Type \"swim\" to swim across: ").lower()

    if action == "wait":
        door = input("You arrived at the island unharmed. There is a house with three doors. "
                     "\nOne red, one yellow and one blue. Which colour do you choose?: ").lower()

        if door == "yellow":
            print("Your found the treasure. You Win!")
        elif door == "red":
            print("Burned by fire. Game Over!")
        elif door == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. Game Over!")
else:
    print("Fell into a hole. Game Over!")
