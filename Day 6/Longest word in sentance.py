# Longest world in the given sentence
def longest_word(sentence):
    
    words = sentence.split()
    
    
    longest = ""
    
    # Iterate over each word
    for word in words:
        
        if len(word) > len(longest):
            longest = word
    
    # Return the longest word
    return longest
sentence = input(str("Enter a sentance:"))
print("The longest word is:", longest_word(sentence))
longest_word(sentence)
