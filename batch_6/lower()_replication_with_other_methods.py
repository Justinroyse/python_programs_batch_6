#initialize function for converting to lowercase 
def lower_case(user_input):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lower_case = "abcdefghijklmnopqrstuvwxyz"

    replacement_table = str.maketrans(upper_case, lower_case)

    return user_input.translate(replacement_table)

#initialize user input
user_input = input("Enter your name: ")

#print result with the function
print(lower_case(user_input))