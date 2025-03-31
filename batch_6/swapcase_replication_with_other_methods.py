# Initialize function for swapcase() replication
def swap_case(user_input):
    user_input_store = []

    for letters in user_input:
        if letters.islower():
            user_input_store.append(letters.upper())
        
        elif letters in user_input:
            user_input_store.append(letters.lower())
        
        else:
            user_input_store.append(letters)
    
    return "".join(user_input_store)


# Initialize user input variable
user_input = input("Enter your desired text: ")

# Print result
print(swap_case(user_input))