# Initialize function for startswith() replication
def check_prefix(user_input, prefix):
    if len(prefix) > len(user_input):
        return False
    
    position = user_input.find(prefix)

    return position == 0


# Initialize user input variable
user_input = input("Enter your desired text: ")
print(user_input)
check_if_prefix = input("Enter the prefix you wish to check for: ")

# Print result
print(check_prefix(user_input, check_if_prefix))

