#for in if-else logic to remove spaces

#initialize user input variable 
user_input = input("Enter your name with 5 spaces beginning: ")

for i in user_input:

    if user_input[0:] == " ":
        user_input.replace(" ", "")

    elif user_input[0:]:
        first_character = user_input.find(chr)
        user_input.replace(" ", " ")

print(user_input)
