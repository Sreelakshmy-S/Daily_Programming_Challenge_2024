# Daily Programming Challenge 2024 : Day 8
# Reverse a String Word by Word
'''
You are given a string s that consists of multiple words separated by spaces. 
Your task is to reverse the order of the words in the string. Words are defined as sequences of non-space characters. 
The output string should not contain leading or trailing spaces, and multiple spaces between words should be reduced to a single space.
'''
string = input()
string = string.strip('""')
sentence = []                   # List stores the words in order
word = ''

for i in string:                # FInds each word
    if i!=' ':
        word += i
    elif word:
        sentence.append(word)   # Appends word to the list
        word = ''               # Initialised to search for next word    
if word:
    sentence.append(word)       # Last word is appended to list

sentence.reverse()              # Reverses the list
s = ' '.join(sentence)          # Stores reversed list elements in the form of string
print('"' + s + '"')                        # Prints string

# Time Complexity : O(n)
# Space Complexity : O(n)