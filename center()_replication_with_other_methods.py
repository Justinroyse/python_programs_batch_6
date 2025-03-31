#initialize function for center() replication
def to_center(user_input, center_spaces):

    if len(user_input) >= center_spaces:
        return user_input
    
    total_spaces = center_spaces - len(user_input)

    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    centered_input = " " * left_spaces + user_input + " " * right_spaces

    return centered_input
    
#initialize user input variable
user_input = input("Enter your desired text to be centered: ")
print(user_input)
center_prompt = int(input("Enter size of center: "))

result = to_center(user_input, center_prompt)

#print result
print(f"'{result}'")
