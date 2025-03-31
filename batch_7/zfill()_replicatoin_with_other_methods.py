#initialize function for zfill() replication
def fill_zero(user_input, fill):
    user_input = str(user_input)

    zeroes_needed = fill - len(user_input)

    if zeroes_needed <= 0:
        return user_input
    
    return "0" * zeroes_needed + user_input

#initialize user input variable and zfill prompt
user_input = input("Enter your desired number: ")
print(user_input)
fill = int(input("Enter your zeroes to fill for: "))

#print result
result = fill_zero(user_input, fill)
print(result)