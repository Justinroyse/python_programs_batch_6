# Initialize function for center() replication
def center_text(user_input, center_spaces):
    if len(user_input) >= center_spaces:
        return user_input

    total_spaces = center_spaces - len(user_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    centered_input = " " * left_spaces + user_input + " " * right_spaces

    return centered_input


# Initialize user input variable
user_input = input("Enter your desired text to be centered: ")
center_prompt = int(input("Enter size of center: "))

result = center_text(user_input, center_prompt)

# Print result
print(f"'{result}'")