from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# BUG - randint will randomly generate an integer between both endpoints (both inclusive)
#       array index starts from 0, therefore is randint generates the number 6
#       we will get IndexError: list index out of range because dice_images[6] is not valid

# to fix this we must do print(dice_images[dice_num] - 1)
