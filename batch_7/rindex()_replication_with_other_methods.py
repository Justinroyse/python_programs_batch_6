# Initialize function for rindex() replication
def find_rindex(user_input, find): 
    find_length = len(find)

    for i in range(len(user_input) - find_length, -1, -1):
        if user_input[i:i + find_length] == find:
            return i
    
    raise ValueError("Not found")


# Initialilze user input variables
user_input = input("Enter your desired text: ")
find = input("Enter word you wish to find first occurence: ")

# Print result
print(find_rindex(user_input, find))
