#intialize user input variable
user_input = input("Enter your fullname with 5 spaces at the beginning: ")

#initialize startswith() function to detect spaces
user_spaces = user_input.startswith(" ")

if user_spaces == True:
     replace = user_input.replace(" ", "")
        
#print result
print(replace)