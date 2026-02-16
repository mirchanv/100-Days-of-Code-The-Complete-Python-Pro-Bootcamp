def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:

# 1. What is the for loop doing?
    # The for loop is going to loop from i=1 to i=19

# 2. When is the function meant to print "You got it"?
    # When i=20 it should print "You got it"

# 3. What are your assumptions about the value of i?
    # it never reaches i=20

# In order to fix the code and get the message printed we must have the for loop running in range(1,21)
