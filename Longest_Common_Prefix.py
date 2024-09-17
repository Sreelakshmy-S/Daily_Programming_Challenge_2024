# Daily Programming Challenge 2024 : Day 9
# Longest Common Prefix
'''
You are given an array of strings strs[], consisting of lowercase letters. 
Your task is to find the longest common prefix shared among all the strings. If there is no common prefix, return an empty string "".
A common prefix is a substring that appears at the beginning of all the strings in the array. 
The task is to identify the longest such prefix that all strings share.
'''

def find_common(arr):
    common = ""
    if not arr:
        return common
    
    common = arr[0]
    for i in arr[1:]:
        while i[:len(common)] != common and common:
            common = common[:-1] 

    if not common: 
        return ""
    
    return common

strings = input("strs[] = ")
strings = strings.strip('[]')
strings = [s.strip().strip('"').strip("'") for s in strings.split(',')]
common = find_common(strings)
print('"' + common + '"')