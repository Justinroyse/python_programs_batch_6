# Initialize function for rjust() replication
def add_left_spaces(user_input, spaces):
    if len(user_input) >= spaces:
        return user_input
    
    spaces_needed = spaces + len(user_input)

    spaced_input = ' ' * spaces_needed + user_input  

    return spaced_input


# Initialize user input variable
user_input = input("Enter your desired text: ")
print(user_input)
spaces = int(input("Enter total spaces needed: "))

# Print result
result = add_left_spaces(user_input, spaces)
print(f"'{result}'")