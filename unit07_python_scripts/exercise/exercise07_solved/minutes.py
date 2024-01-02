# ask the user for input; save their input into a variable called "age"
age = input("How old are you? ")

# convert into a float
age = float(age)

# multiply by *365 (days) *24 (hours) *60 (minutes)
age_minutes = age * 365 * 24 * 60

# optional: round (to obtain an integer value)
age_minutes = round(age_minutes)

# print out the result
print(f"Your age in minutes is: {age_minutes}")
