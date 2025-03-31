#initialize function for count() replication
def count_occurred(user_input, counting):
    count = 0

    counting_length = len(counting)

    for i in range(len(user_input) - counting_length + 1):
        if user_input[i:i + counting_length] == counting:
            count += 1
    
    return count

#initialize user input variable
user_input = input("Enter your desired text: ")
counting = input("Enter word/words to count for: ")

#print result
result = count_occurred(user_input, counting)
print(result)