# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

#function to check if two words are anagrams or not
def find_anagram(word, anagram):
    # [assignment] Add your code here
    # the two strings are sorted then checked
    if(sorted(word)== sorted(anagram)):
        print("The two words are anagrams of each other")
        return True
    else:
        print("The two words are not anagrams of each other")
        return False

#User enters the first word    
print("Enter the first word")
word_one = input()
word_one = str(word_one)

#User enters the second word
print("Enter the second word")
word_two = input()
word_one = str(word_two)

#The function to check if the two words are anagrams is called
find_anagram(word_one, word_two)