# Initialize function for islower() replication
def check_lower(user_input):
    if not user_input:
        return False
    
    for letters in user_input:
        if letters.isalpha() and not ("a" <= letters <= "z"):
            return False
    
    return True


# Initialize user input variable
user_input = input("Enter your desired text: ")

# Print boolean result
print(check_lower(user_input))