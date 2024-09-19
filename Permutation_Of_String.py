# Daily Programming Challenge 2024 : Day 11
# Permutations of a String
'''
You are given a string s. 
Your task is to generate and return all possible permutations of the characters in the string. 
A permutation is a rearrangement of the characters in the string, and each character must appear exactly once in every permutation. 
If there are duplicate characters in the string, the resulting permutations should also be unique.
'''
from itertools import permutations

def permute(arr):
    permute = set(permutations(arr))
    permute = [''.join(p) for p in permute]
    return permute

string = input()
string = string.strip('""')
ans = permute(string)
print(ans)