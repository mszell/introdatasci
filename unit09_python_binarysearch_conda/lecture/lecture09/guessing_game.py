left_limit = 1
right_limit = 1000

print(f"Think of a number between {left_limit} and {right_limit}!")
count = 0
while True:
    middle = (left_limit + right_limit) // 2

    user_input = input(f"Is the number {middle}; lower; or higher? (Y/L/H) ")
    user_input = user_input.upper()
    while user_input not in ["Y", "L", "H"]:
        user_input = input(f"Sorry, I didn't understand your input. Is the number {middle}; lower; or higher? (Y/L/H) ")
        user_input = user_input.upper()
    
    count += 1
    if user_input == "Y":
        print(f"Game over. I found the number in {count} questions!")
        break    
    elif user_input == "H":
        left_limit = middle + 1
    else:
        right_limit = middle - 1