#initialize function for endswith() replication
def check_suffix(user_input, suffix):
    suffix = user_input.find(suffix, -1)

    if suffix == True:
        return True
    else:
        return False

#initialize user input variable
user_input = input("Enter your desired text: ")
print(user_input)
suffix = input("Enter the suffix you wish to check for: ")

#print result
print(check_suffix(user_input, suffix))