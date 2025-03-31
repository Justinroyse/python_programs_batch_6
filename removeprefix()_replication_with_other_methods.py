#intialize function for removeprefix() replication
def remove_prefix(removed_word):
    remove = removed_word.replace(removed_word, "pogi")

    return remove

#initialize user input 
sample_text = "JustinPogi"

print(sample_text)

user_input = input("Select word/s that you would like to remove: ")

#print result

print(remove_prefix(user_input))
