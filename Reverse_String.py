# Daily Programming Challenge 2024 : Day 8
# Reverse a String Word by Word

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