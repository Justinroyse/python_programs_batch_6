#initialize function to check for upper_case letters and return boolean
def check_upper(user_input):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if len(user_input) in upper_case:
        return True
    else:
        return False

#initialize user input
user_input = input("Enter your desired text: ")

#print result
print(check_upper(user_input))