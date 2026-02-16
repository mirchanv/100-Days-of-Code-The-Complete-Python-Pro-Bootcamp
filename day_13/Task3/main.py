year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# problem/bug - the year 1994 will not print anything
# to fix this we must change < to <= 1994 on line3