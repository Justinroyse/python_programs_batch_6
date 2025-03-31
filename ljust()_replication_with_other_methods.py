#initialize function fo ljust() replication
def add_right_spaces(user_input, spaces):
    if len(user_input) >= spaces:
        return user_input
    
    spaces_needed = spaces - len(user_input)

    spaced_input = user_input + ' ' * spaces_needed

    return spaced_input

#initialize user input
user_input = input("Enter your desired text: ")
spaces = int(input("Enter the total spaces needed: "))

result = add_right_spaces(user_input, spaces)

#print result
print(f"'{result}'")

