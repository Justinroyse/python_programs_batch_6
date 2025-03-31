#intialize function for removeprefix() replication
#initialize a startswith() function to check for prefix and remove it
def remove_prefix(user_input, remove):
    if user_input.startswith(remove):
        return user_input[len(remove):]
    else:
        return user_input
    
#initialize user input and prompt on what to remove
user_input = input("Enter your desired text: ")

print(user_input)

remove_word = input("Type the prefix on what you want to remove: ")

#print result
print(remove_prefix(user_input, remove_word))
