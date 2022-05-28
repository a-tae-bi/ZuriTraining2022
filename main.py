# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string


def read_file_content(filename):
    # [assignment] Add your code here 
    read_file = open(filename, "r")
    return(read_file)


def count_words():
    text = read_file_content("./story.txt")
   
    # [assignment] Add your code here
    my_dictionary = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
  
        # Convert the characters in line to 
        # lowercase to avoid case mismatch
        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))
  
        # Split the line into words
        words = line.split(" ")
  
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in my_dictionary:
                # Increment count of word by 1
                my_dictionary[word] = my_dictionary[word] + 1
            else:
                # Add the word to dictionary with count 1
                my_dictionary[word] = 1
    
    # Print the contents of dictionary
    for key in list(my_dictionary.keys()):
        print(key, ":", my_dictionary[key])

count_words()

