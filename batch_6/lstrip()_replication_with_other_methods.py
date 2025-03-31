#intialize function for lstrip replication
#initialize a loop to find non-space character
def remove_spaces_left(user_input):
    
     user_input_string = 0

     while user_input_string < len(user_input) and user_input[user_input_string] == " ":
          user_input_string += 1
     
     return user_input[user_input_string:]

#intialize user input
user_input = input("Enter your fullname with 5 spaces at the beginning: ")

#print result using function
print(remove_spaces_left(user_input))
