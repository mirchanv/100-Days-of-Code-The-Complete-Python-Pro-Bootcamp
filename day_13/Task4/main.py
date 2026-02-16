age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")

# indentation error after if statement - need to fix by indenting
# age not printed correctly - need to fix by making use of Fstring

"""
Catching Exceptions
You can use a try/except block in Python to catch any exceptions that might occur. 
For example if you imagine there could be a chance of user error. 
You can prevent it crashing your code by anticipating it. 
You trap the dangerous code inside a try block and use an except block to catch any potential errors. 
Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.

e.g.
try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")
"""