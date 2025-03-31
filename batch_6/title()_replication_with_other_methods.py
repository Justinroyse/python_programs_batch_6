# Initialize function for title() replicaton
def to_title(user_input):
    words = user_input.split()

    corrected_words = []

    for word in words: 
        if word: 
            corrected_word = word[0].upper() + word[1:].lower()
            corrected_words.append(corrected_word)
    
    return " ".join(corrected_words)


# Initialize user input variable
user_input = input("Enter your desired text: ")

# Print result
print(to_title(user_input))