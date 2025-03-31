# Initialize function for removeprefix() replication
# Initialize a startswith() function to check for prefix and remove it
def remove_prefix(user_input, remove):
    if user_input.startswith(remove):
        return user_input[len(remove):]
    return user_input


# Initialize user input and prompt on what to remove
user_input = input("Enter your desired text: ")
remove_word = input("Type the prefix on what you want to remove: ")

# Print result
print(remove_prefix(user_input, remove_word))
