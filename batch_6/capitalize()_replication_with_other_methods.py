#initialize function for capitalize() replication
def capital_first(user_input):
    if not user_input: 
        return user_input
    
    first_letter = user_input[0].upper()
    other_letters = user_input[1:].lower()

    return first_letter + other_letters


#initialize user input
user_input = input("Enter your desired text: ")

#print result
print(capital_first(user_input))