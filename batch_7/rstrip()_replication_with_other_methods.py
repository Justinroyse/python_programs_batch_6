# Initialize function for rstrip() replication
def rm_right_spaces(user_input):
    user_input_string = len(user_input) - 1

    while user_input_string >= 0 and user_input[user_input_string] == " ":
        user_input_string -= 1 
     
    return user_input[:user_input_string + 1]

# Initialize user input
user_input = input("Enter your desired text: ")

# Print result
result = rm_right_spaces(user_input)
print(f"'{result}'")