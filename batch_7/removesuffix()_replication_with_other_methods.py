#initialize function for removesuffix() replication
#initialize a endswith() function to check for suffix and remove it
def remove_suffix(user_input, remove):
    if user_input.endswith(remove):
        return user_input[:-len(remove)]
    else:
        return user_input
    
#initialize user input variable
user_input = input("Enter your desired text: ")
print(user_input)
remove_words = input("Enter prefix to remove: ")

#print result
print(remove_suffix(user_input, remove_words))