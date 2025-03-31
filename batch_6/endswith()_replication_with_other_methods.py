# Initialize function for endswith() replication
def check_suffix(user_input, suffix):
    suffix_length = len(suffix)

    if len(user_input) < suffix_length:
        return False

    position = user_input.find(suffix)

    return position == len(user_input) - suffix_length


# Initialize user input variable
user_input = input("Enter your desired text: ")
suffix = input("Enter the suffix you wish to check for: ")

# Print result
print(check_suffix(user_input, suffix))