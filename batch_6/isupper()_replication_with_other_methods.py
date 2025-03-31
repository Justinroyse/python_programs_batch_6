#initialize function to check for upper_case letters and return boolean
def check_upper(user_input):
    if not user_input:
        return False
    
    for letters in user_input:
        if letters.isalpha() and not ("A" <= letters <= "Z"):
            return False
    
    return True

#initialize user input
user_input = input("Enter your desired text: ")

#print result
print(check_upper(user_input))