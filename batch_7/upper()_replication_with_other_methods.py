#initialize function for upper() replication
#initialize list for storing result of converted letters
def make_upper(user_input):
    result = []

    for letter in user_input:
        if 'a' <= letter <= 'z':
            uppercase_letter = chr(ord(letter) - (ord('a') - ord('A')))
            result.append(uppercase_letter)
        
        else:
            result.append(letter)
    
    return ''.join(result)

#initialize user input variable
user_input = input("Enter your desired text: ")

#print result
print(make_upper(user_input))