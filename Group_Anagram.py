# Daily Programming Challenge 2024 : Day 10
# Group Anagrams
'''
You are given an array of strings strs[]. 
Your task is to group all the strings that are anagrams of each other. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
The goal is to return the grouped anagrams as a list of lists, where each sublist contains words that are anagrams of each other.
'''
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:                               # Sort the string and use it as a key
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    
    return list(anagrams.values())

strs = input("strs[] = ")
strs = strs.strip('[]')
strs = [s.strip().strip('"').strip("'") for s in strs.split(',')]
print(group_anagrams(strs))

# Time Complexity : O(nlogn)
# Space Complexity : O(n)