print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill += (tip / 100) * bill
bill_per_person = (bill / people)
print(f"Each person should pay: ${bill_per_person:.2f}")

# When it comes to float numbers, you can use format specifiers:
# f'{value:<width>.<precision>}'
    # value is any expression that evaluates to a number
    # width specifies the number of characters used in total to display, but if value needs more space than the width specifies then the additional space is used.
    # precision indicates the number of characters used after the decimal point

