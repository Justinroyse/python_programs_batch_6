# Initialize function for upper() replication
# Initialize list for storing result of converted letters
def make_upper(user_input):
    result = []

    for letter in user_input:
        if 'a' <= letter <= 'z':
            uppercase_letter = chr(ord(letter) - (ord('a') - ord('A')))
            result.append(uppercase_letter)
        
        else:
            result.append(letter)
    
    return ''.join(result)


# Initialize user input variable
user_input = input("Enter your desired text: ")

# Print result
print(make_upper(user_input))